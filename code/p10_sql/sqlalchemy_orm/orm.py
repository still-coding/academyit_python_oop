from datetime import datetime
from sqlalchemy import ForeignKey, Identity, create_engine, select
from sqlalchemy.orm import DeclarativeBase, mapped_column, relationship
from sqlalchemy.orm import sessionmaker
from sqlalchemy.types import DateTime, Integer, Numeric, String
from random import choice, sample, randint


class Base(DeclarativeBase): 
    pass

class Customer(Base):
    __tablename__ = 'customers'
    id = mapped_column(Integer, Identity(), primary_key=True)
    name = mapped_column(String(50), nullable=False)
    address = mapped_column(String, nullable=False)
    orders = relationship('Order', back_populates='customer')

    def __repr__(self):
        return f'<Customer id={self.id} name={self.name}>'


class Order(Base):
    __tablename__ = 'orders'
    id = mapped_column(Integer, Identity(), primary_key=True)
    customer_id = mapped_column(Integer, ForeignKey('customers.id'), nullable=False)
    number = mapped_column(String(10), nullable=False)
    time = mapped_column(DateTime, nullable=False)
    customer = relationship('Customer', back_populates='orders')
    details = relationship('OrderDetails', back_populates='order')

    def __repr__(self):
        return f'<Order id={self.id} cust_id={self.customer_id}>'


class Product(Base):
    __tablename__ = 'products'
    id = mapped_column(Integer, Identity(), primary_key=True)
    name = mapped_column(String(50), nullable=False)
    price = mapped_column(Numeric(8, 2), nullable=False)
    details = relationship('OrderDetails', back_populates='product')

    def __repr__(self):
        return f'<Product id={self.id} price={self.price}>'


class OrderDetails(Base):
    __tablename__ = 'order_details'
    order_id = mapped_column(Integer, ForeignKey('orders.id'), primary_key=True)
    product_id = mapped_column(Integer, ForeignKey('products.id'), primary_key=True)
    quantity = mapped_column(Numeric(6, 2), nullable=False)
    order = relationship('Order', back_populates='details')
    product = relationship('Product', back_populates='details')

    def __repr__(self):
        return f'<OrderDetails order_id={self.order_id} product_id={self.product_id}>'



def get_session_engine(db_uri):
    engine = create_engine(db_uri)
    session = sessionmaker(engine)
    return session, engine


def create_database(db_uri):
    session, engine = get_session_engine(db_uri)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    return session


def fill_db(sess):
    def read_csv(filename):
        with open(filename, 'r') as f:
            result = [line.strip() for line in f]
        return [line.split(';') for line in result]

    customers = read_csv("customers.csv")
    products = read_csv("products.csv")


    with sess() as session, session.begin():
        for cust in customers:
            c = Customer(
                name=cust[0],
                address=cust[1],
            )
            session.add(c)
        for prod in products:
            p = Product(
                name=prod[0],
                price=prod[1],
            )
            session.add(p)
    
    with sess() as session, session.begin():
        cust_ids = [c.id for c in session.scalars(select(Customer)).all()]

        for i in range(100):
            o = Order(
                customer_id=choice(cust_ids),
                number=i,
                time=datetime.now(),
            )
            session.add(o)

    with sess() as session, session.begin():
        prod_ids = [c.id for c in session.scalars(select(Product)).all()]
        order_ids = [c.id for c in session.scalars(select(Order)).all()]

        for order_id in order_ids:
            currend_order_product_ids = sample(prod_ids, randint(1, 50))
            for product_id in currend_order_product_ids:
                det = OrderDetails(
                    order_id=order_id,
                    product_id=product_id,
                    quantity=randint(1, 1000)
                )
                session.add(det)


def execute_query(sess, query):
    return sess().execute(query).all()


if __name__ == '__main__':
    DB_URI = "sqlite:///shop.db"
    sess = create_database(DB_URI)
    fill_db(sess)

    q = select(Customer)

    customer = execute_query(sess, q)[3][0]
    print(customer)
    total = 0
    for order in customer.orders:
        for details in order.details:
            total += details.product.price * details.quantity
    print(total)


