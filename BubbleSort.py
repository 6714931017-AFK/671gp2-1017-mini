class BubbleSorter:
    @staticmethod
    def sort_by_box_office(movie_list, descending=True):
        """เรียงตามรายได้หนัง"""
        arr = list(movie_list)
        n = len(arr)
        for i in range(n):
            swapped = False
            for j in range(0, n - i - 1):
                condition = (arr[j].box_office_m < arr[j + 1].box_office_m) if descending else (arr[j].box_office_m > arr[j + 1].box_office_m)
                if condition:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swapped = True
            if not swapped:
                break
        return arr

    @staticmethod
    def sort_by_year(movie_list, descending=True):
        """เรียงตามปีที่ฉาย"""
        arr = list(movie_list)
        n = len(arr)
        for i in range(n):
            swapped = False
            for j in range(0, n - i - 1):
                condition = (arr[j].release_year < arr[j + 1].release_year) if descending else (arr[j].release_year > arr[j + 1].release_year)
                if condition:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swapped = True
            if not swapped:
                break
        return arr

    @staticmethod
    def sort_by_rating(movie_list, descending=True):
        """เรียงตามคะแนน IMDb"""
        arr = list(movie_list)
        n = len(arr)
        for i in range(n):
            swapped = False
            for j in range(0, n - i - 1):
                condition = (arr[j].rating < arr[j + 1].rating) if descending else (arr[j].rating > arr[j + 1].rating)
                if condition:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swapped = True
            if not swapped:
                break
        return arr