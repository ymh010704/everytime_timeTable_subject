# 사용자의 ID와 PW는 임의로 구현했다.
# ID : student
# PW : 1234

class LectureDB:
    # 강의 정보를 담을 임시 강의 DB
    def __init__(self):
        self.lectures = {
            "소프트웨어공학": {"교수": "정용훈 교수님", "시간": "월 3-6교시", "장소": "성결관 404호"},
            "사회봉사": {"교수": "김사회 교수님", "시간": "월 7-7교시", "장소": "영암관 201호"},
            "웹응용기술": {"교수": "이응용 교수님", "시간": "화 3-6교시", "장소": "성결관 407호"},
            "모바일프로그래밍": {"교수": "모바일 교수님", "시간": "화 7-9교시", "장소": "성결관 405호"},
            "채플": {"교수": "정채플 교수님", "시간": "목 2-2교시", "장소": "기념관 501호"},
            "컴퓨터알고리즘": {"교수": "임컴알 교수님", "시간": "목 4-6교시", "장소": "성결관 407호"},
            "인공지능": {"교수": "한인공 교수님", "시간": "목 7-9교시", "장소": "성결관 406호"},
        }

    def get_lecture_info(self, lecture_name):
        return self.lectures.get(lecture_name, "해당 강의를 찾을 수 없습니다.")


class EverytimeApp:
    def __init__(self):
        self.db = LectureDB()
        self.time_table = ["소프트웨어공학", "사회봉사", "웹응용기술", "모바일프로그래밍", "채플", "컴퓨터알고리즘", "인공지능"]

    def login(self):
        while True:
            user_id = input("ID를 입력하세요: ")
            password = input("비밀번호를 입력하세요: ")
            # 로그인 기능 느낌 내도록 student, 1234로 임시 구현
            if user_id == "student" and password == "1234":
                print(f"\n✅ {user_id}님 로그인 되었습니다!")
                break
            else:
                print("❌ 로그인 실패. 다시 시도하세요.\n")

    def view_time_table(self):
        # 내 시간표 테이블 목록 나열
        print("\n📅 나의 시간표:")
        for i, lecture in enumerate(self.time_table, 1):
            print(f"{i}. {lecture}")

    def show_lecture_info(self, index):
        lecture_name = self.time_table[index - 1]
        info = self.db.get_lecture_info(lecture_name)
        print(f"\n📘 {lecture_name} 수업의 강의 정보:")
        for key, value in info.items():
            print(f"- {key}: {value}")


# 실행 예시
app = EverytimeApp()
app.login()

while True:
    app.view_time_table()

    while True:
        try:
            choice = int(input("\n상세정보를 볼 강의 번호를 선택하세요: "))
            if choice < 1 or choice > len(app.time_table):
                raise IndexError
            app.show_lecture_info(choice)
            break
        except (ValueError, IndexError):
            print("⚠️ 잘못된 입력입니다. 다시 시도해주세요.")

    more = input("\n📖 다른 강의 정보를 더 보시겠습니까? (y/n): ").strip().lower()
    if more != 'y':
        print("\n👋 모든 정보를 확인했습니다!")
        break
