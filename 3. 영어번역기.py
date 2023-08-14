from googletrans import Translator


def translator(input_file_path, output_file_path, encoding="UTF-8"):
  translator = Translator()
  
  if not input_file_path or not output_file_path:
    return "파일 경로를 입력해주세요!"

  # 파일 읽기
  with open(input_file_path, "r", encoding=encoding) as input_file:
    text = input_file.read()

  # 번역
  result = translator.translate(text, dest="ko")

  # 번역한 결과를 파일에 쓰기
  with open(output_file_path, "w", encoding=encoding) as output_file:
    output_file.write(result.text)
  
  return "파일 저장 성공"


print(translator("docs/english.txt", "docs/korean.txt"))