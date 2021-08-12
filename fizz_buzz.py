class FizzBuzzSolution:
    @staticmethod
    def print_fizz_buzz_range(total_count):
        """
        This function takes total count for the range of integers that needs to be considered.
        It will print Fizz if number is divisible by 3,
        Buzz if divisible by 5 and FizzBuzz if divisible by both 3 and 5
        :param total_count: Total count for the range of integers that needs to be considered
        :return: None
        """
        if total_count <= 0:
            return "Please pass value greater than 0"

        for i in range(1, total_count+1):
            print("Fizz" * (i % 3 == 0) + "Buzz" * (i % 5 == 0) or str(i))
            
            
FizzBuzzSolution.print_fizz_buzz_range(100)
