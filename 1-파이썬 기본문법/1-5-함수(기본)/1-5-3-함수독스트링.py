def remove_space(words):
    """전달받은 인자(문자열)의 앞 뒤 공백을
    정리한 값을 반환합니다."""
    return words.strip()


s = input("문자열 입력 : ")
print(remove_space(s))

print(remove_space.__doc__)
help(remove_space)
"""함수 독스트링(docstring):
파이썬에선 함수정의 시에, 콜론: 바로 다음 줄에 """"""(문자열 주석)으로 함수에 대한 설명을 넣을 수 있는데,
이런 문자열을 독스트링(= 문서화 문자열, documentation strings, docstrings(독스트링))이라고 함.
(대신 독스트링 위에 다른 코드가 오면 안됨, 독스트링이 가장 먼저)

물론 '', "", '''''' 을 활용해서 만들어도 되지만, PEP 8(코딩스타일규칙)에서는 큰따옴표 세개를 활용하는 걸 권장한다.

독스트링은 함수의 사용방법만 기록하고, 함수의 코드에는 영향을 주지 않는데, 
함수이름.__doc__ 와 같이하면, 함수의 독스트링을 반환할 수 있다.

아니면 heip(함수이름)과 같이, help()함수에 함수이름을 넣으면,
인자값으로 받은 함수의 독스트링을 도움말 형태로 출력할 수 있다.
"""