import datetime
from dateutil.relativedelta import relativedelta


class Solution:
    @staticmethod
    def exercise_1():
        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), end="")

    @staticmethod
    def exercise_2(date_string: str):
        print(datetime.datetime.strptime(date_string, "%b %d %Y %I:%M%p"), end="")

    @staticmethod
    def exercise_3(
        given_date: datetime.datetime, days_to_substract: int
    ) -> datetime.datetime:
        return given_date - datetime.timedelta(days=days_to_substract)

    @staticmethod
    def exercise_4(given_date: datetime.datetime) -> str:
        return given_date.strftime("%A %d %B %Y")

    @staticmethod
    def exercise_5(given_date: datetime.datetime) -> str:
        return given_date.strftime("%A")

    @staticmethod
    def exercise_6(given_date: datetime.datetime) -> str:
        return (given_date + datetime.timedelta(days=7, hours=12)).strftime(
            "%Y-%m-%d %H:%M:%S"
        )

    @staticmethod
    def exercise_9(given_date: datetime.date, months_to_add: int) -> str:
        result = given_date + relativedelta(months=months_to_add)
        return result.strftime("%Y-%m-%d")
