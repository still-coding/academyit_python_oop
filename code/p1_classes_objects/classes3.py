class Singleton:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            __instance = super().__new__(cls, *args, **kwargs)
        return cls.__instance




