import sys
import os
import database

class Library:

    def __init__(self, Booklist):
        self.Booklist = Booklist
        self.User_Add_Booklist = []
        self.Book = []
        self.User_Book_Search = []

    def Menu(self):
        try:
            print("1. 도서 추가")
            print("2. 도서 검색")
            print("3. 도서 정보 수정")
            print("4. 도서 삭제")
            print("5. 현재 총 도서 목록 출력")
            print("6. 작업한 내용 저장")
            print("7. 프로그램 종료")
            invalue = int(input("입력 : "))

            if invalue == 1:
                self.Addbook() #추가
            elif invalue == 2:
                self.search() #검색
            elif invalue == 3:
                self.modify() #수정
            elif invalue == 4:
                self.DeleteBook() #삭제
            elif invalue == 5:
                self.ShowBook() #목록 확인
            elif invalue == 6:
                self.Save() #저장
            elif invalue == 7:
                self.ProgramExit() #자동 저장 종료
            else:
                print("1부터 7까지의 숫자만 입력하세요.")
                return self.Menu()
        except ValueError:
            print("잘못입력하셨습니다.")
            return self.Menu()    

    def Addbook(self):
        print("도서 추가")
        print("도서명 저자 출판연도 출판사명 장르")
        UserInput = list(map(str,input("입력 : ").split()))
        self.Booklist.append(UserInput)
        self.User_Add_Booklist.append(UserInput)
        print("도서가 추가되었습니다")
        return self.Menu()

    def search(self):
        print("1.도서명 2.저자 3.출판년도 4.출판사명 5.장르(이외의 입력은 메뉴로 돌아가용)")
        search_num = int(input("숫자입력 : "))
        if search_num == 1:
            UserInput1 = str(input("도서명 입력 : "))
            for i in range(len(self.Booklist)):
                if UserInput1 == self.Booklist[i][0]:                    
                    print(self.Booklist[i])
            choice1 = input("1.검색을 계속합니다.\n2.메뉴로 돌아갑니다. \n입력: ")
            if choice1 == 1:
                return self.search()
            elif choice1 == 2:
                return self.Menu()
            elif ValueError:
                print("잘못된 입력입니다. 검색으로 돌아갑니다.")
                return self.search()
        elif search_num == 2:
            UserInput2 = str(input("저자 입력 : "))
            for i in range(len(self.Booklist)):
                if UserInput2 == self.Booklist[i][1]:
                    print(self.Booklist[i])
            return self.search()
            choice1 = input("1.검색을 계속합니다.\n2.메뉴로 돌아갑니다. \n입력: ")
            if choice1 == 1:
                return self.search()
            elif choice1 == 2:
                return self.Menu()
            elif ValueError:
                print("잘못된 입력입니다. 검색으로 돌아갑니다.")
                return self.search()
        elif search_num == 3:
            UserInput3 = str(input("출판년도 입력 : "))
            for i in range(len(self.Booklist)):
                if UserInput3 == self.Booklist[i][2]:
                    print(self.Booklist[i])
            return self.search()
            choice1 = input("1.검색을 계속합니다.\n2.메뉴로 돌아갑니다. \n입력: ")
            if choice1 == 1:
                return self.search()
            elif choice1 == 2:
                return self.Menu()
            elif ValueError:
                print("잘못된 입력입니다. 검색으로 돌아갑니다.")
                return self.search()
        elif search_num == 4:
            UserInput3 = str(input("출판사 입력 : "))
            for i in range(len(self.Booklist)):
                if UserInput3 == self.Booklist[i][3]:
                    print(self.Booklist[i])
            return self.search()
            choice1 = input("1.검색을 계속합니다.\n2.메뉴로 돌아갑니다. \n입력: ")
            if choice1 == 1:
                return self.search()
            elif choice1 == 2:
                return self.Menu()
            elif ValueError:
                print("잘못된 입력입니다. 검색으로 돌아갑니다.")
                return self.search()
        elif search_num == 5:
            UserInput3 = str(input("장르 입력 : "))
            for i in range(len(self.Booklist)):
                if UserInput3 == self.Booklist[i][4]:
                    print(self.Booklist[i])
            return self.search()
            choice1 = input("1.검색을 계속합니다.\n2.메뉴로 돌아갑니다. \n입력: ")
            if choice1 == 1:
                return self.search()
            elif choice1 == 2:
                return self.Menu()
            elif ValueError:
                print("잘못된 입력입니다. 검색으로 돌아갑니다.")
                return self.search()    
        else:
            return self.Menu()

    def modify(self):
        print("도서 정보 수정")
        UserInput = str(input("수정할 도서명을 입력해주세요. \n입력: "))
        for i in range(len(self.Booklist)):    
            if UserInput == self.Booklist[i][0]:
                print("수정할 정보입력")
                UserInput_MDY = list(map(str, input("도서명 저자 출판일 출판사명 장르 (입력) :").split()))
                del self.Booklist[i]
                self.Booklist.insert(i, UserInput_MDY) ##i번째에 있는 정보를 삭제하고 그 자리에 변경한 정보를 끼워넣는다.
                print("수정 완료")
                return self.Menu()
            else:
                if i == len(self.Booklist):
                    print("수정할 도서가 없습니다.")
        return self.Menu()
        

    def DeleteBook(self):
        print("도서 삭제")
        UserInput = str(input("도서명 입력 : "))
        for i in range(len(self.Booklist)):
            if UserInput == self.Booklist[i][0]:
                del self.Booklist[i]
                print("도서 삭제 완료")
                return self.Menu()
            else:
                if i == len(self.Booklist):
                    print("목록에 없는 도서입니다.")
        return self.Menu()

    def ShowBook(self):
        for i in range(len(self.Booklist)):
            print(self.Booklist[i])
        value = input("아무키나 입력하고 엔터를 누르면 메뉴로 돌아갑니다.")
        if value == 1:
            return self.Menu()
        else:
            return self.Menu()

    def ProgramExit(self):
        print("프로그램을 종료합니다.")
        sys.exit()

    def Save(self):
        THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
        my_file = os.path.join(THIS_FOLDER, 'input.txt')
        Bookdata = open(my_file, 'w')
        UserInput = str(input("이때까지 내용들을 저장하시겠습니까? (y/n) : "))
        if UserInput == 'y':
            for i in range(len(self.Booklist)):
                Bookdata.writelines(" ".join(self.Booklist[i]))
                Bookdata.write("\n")
            print("저장완료")
            return self.Menu()
        elif UserInput == 'n':
            print("메뉴로 돌아갑니다.")
            return self.Menu()
        else:
            print("잘못 입력하셨습니다.")
            return self.Save()
        Bookdata.close()

        
operate = database.BookList()
operate.Booklist_Get()
BookSystem = Library(operate.Booklist)
BookSystem.Menu()
