#!C:\Users\minjun\anaconda3\python.exe
# -*- coding: UTF-8 -*-
print("Content-type:text/html")
print()

import script

desc = '''
<div class="container_id">
  <h2>Source</h2>
  <p><strong><u>content</u></strong><br><br>
    초상화	https://namu.wiki/w/%EC%B4%88%EC%83%81%ED%99%94<br>
    수채화	https://namu.wiki/w/%EC%88%98%EC%B1%84%ED%99%94<br>
    캘리그라피	https://namu.wiki/w/%EC%BA%98%EB%A6%AC%EA%B7%B8%EB%9E%98%ED%94%BC?from=%EC%BA%98%EB%A6%AC%EA%B7%B8%EB%9D%BC%ED%94%BC<br>
    pop	https://namu.wiki/w/POP<br>
    유화	https://namu.wiki/w/%EC%9C%A0%ED%99%94(%EB%AF%B8%EC%88%A0)<br>
    벽화	https://namu.wiki/w/%EB%B2%BD%ED%99%94<br>
    서예	https://namu.wiki/w/%EC%84%9C%EC%98%88<br>
    수목화	https://namu.wiki/w/%ED%95%9C%EA%B5%AD%ED%99%94?from=%EC%88%98%EB%AC%B5%ED%99%94<br>
    사군자	https://namu.wiki/w/%EC%82%AC%EA%B5%B0%EC%9E%90<br>
    컴퓨터그래픽	https://namu.wiki/w<br>/%EC%BB%B4%ED%93%A8%ED%84%B0%20%EA%B7%B8%EB%9E%98%ED%94%BD%EC%8A%A4
    3d컴퓨터그래픽	https://namu.wiki/w/%EC%BB%B4%ED%93%A8%ED%84%B0%20%EA%B7%B8%EB%9E%98%ED%94%BD%EC%8A%A4<br>
    포토샵	https://namu.wiki/w/%EC%96%B4%EB%8F%84%EB%B9%84%20%ED%8F%AC%ED%86%A0%EC%83%B5<br>
    일러스트	https://namu.wiki/w/%EC%9D%BC%EB%9F%AC%EC%8A%A4%ED%8A%B8%EB%A0%88%EC%9D%B4%ED%84%B0<br>
    모션그래픽	https://namu.wiki/w/%EB%AA%A8%EC%85%98%20%EA%B7%B8%EB%9E%98%ED%94%BD<br>
    게임 그래픽	https://namu.wiki/w/%EA%B2%8C%EC%9E%84%20%EA%B7%B8%EB%9E%98%ED%94%BD%20%EB%94%94%EC%9E%90%EC%9D%B8<br>
    사진 촬영(풍경, 인물)	https://namu.wiki/w/%EC%B4%AC%EC%98%81<br>
    외발자전거	https://namu.wiki/w/%EC%99%B8%EB%B0%9C%EC%9E%90%EC%A0%84%EA%B1%B0<br>
    인라인 	https://namu.wiki/w/%EC%9D%B8%EB%9D%BC%EC%9D%B8%20%EC%8A%A4%EC%BC%80%EC%9D%B4%ED%8A%B8<br>
    스케이트보드	https://namu.wiki/w/%EC%8A%A4%EC%BC%80%EC%9D%B4%ED%8A%B8%EB%B3%B4%EB%93%9C<br>
    자전거	https://namu.wiki/w/%EC%9E%90%EC%A0%84%EA%B1%B0<br>
    등산	https://namu.wiki/w/%EB%93%B1%EC%82%B0<br>
    마라톤	https://namu.wiki/w/%EB%A7%88%EB%9D%BC%ED%86%A4<br>
    수영	https://namu.wiki/w/%EC%88%98%EC%98%81<br>
    스킨스쿠버,스노클링	https://namu.wiki/w/%EC%8A%A4%EB%85%B8%ED%81%B4%EB%A7%81<br>
    권투,검도	https://namu.wiki/w/%EA%B6%8C%ED%88%AC<br>
    펜싱	https://namu.wiki/w/%ED%8E%9C%EC%8B%B1<br>
    암벽타기	https://namu.wiki/w/%EC%95%BC%EB%A7%88%EC%B9%B4%EC%8B%9C<br>
    요트	https://namu.wiki/w/%EC%9A%94%ED%8A%B8<br>
    권투	https://namu.wiki/w/%ED%81%AC%EB%A3%A8%EC%A0%B8%EB%B3%B4%EB%93%9C<br>
    검도	https://namu.wiki/w/%EA%B2%80%EB%8F%84<br>
    펜싱	https://namu.wiki/w/%ED%8E%9C%EC%8B%B1<br>
    철인 3종	https://namu.wiki/w/%ED%8A%B8%EB%9D%BC%EC%9D%B4%EC%95%A0%EC%8A%AC%EB%A1%A0?from=%EC%B2%A0%EC%9D%B83%EC%A2%85%EA%B2%BD%EA%B8%B0<br>
    패러글라이딩	https://namu.wiki/w/%ED%8C%A8%EB%9F%AC%EA%B8%80%EB%9D%BC%EC%9D%B4%EB%94%A9<br>
    스키	https://namu.wiki/w/%EC%8A%A4%ED%82%A4<br>
    보드	https://namu.wiki/w/%EB%B3%B4%EB%93%9C<br>
    수상스키	https://namu.wiki/w/%EC%88%98%EC%83%81%EC%8A%A4%ED%82%A4<br>
    요가	https://namu.wiki/w/%EC%9A%94%EA%B0%80<br>
    승마	https://namu.wiki/w/%EC%8A%B9%EB%A7%88<br>
    헬스	https://namu.wiki/w/%ED%97%AC%EC%8A%A4<br>
    걷기	https://namu.wiki/w/%EA%B1%B7%EA%B8%B0<br>
    야구 	https://namu.wiki/w/%EC%95%BC%EA%B5%AC<br>
    농구	https://namu.wiki/w/%EB%86%8D%EA%B5%AC<br>
    축구	https://namu.wiki/w/%EC%B6%95%EA%B5%AC<br>
    풋살	https://namu.wiki/w/%ED%92%8B%EC%82%B4<br>
    족구	https://namu.wiki/w/%EC%A1%B1%EA%B5%AC<br>
    골프	https://namu.wiki/w/%EA%B3%A8%ED%94%84<br>
    테니스	https://namu.wiki/w/%ED%85%8C%EB%8B%88%EC%8A%A4<br>
    게이트볼	https://namu.wiki/w/%EA%B2%8C%EC%9D%B4%ED%8A%B8%EB%B3%BC<br>
    탁구	https://namu.wiki/w/%ED%83%81%EA%B5%AC<br>
    당구	https://namu.wiki/w/%EB%8B%B9%EA%B5%AC<br>
    포켓볼	https://namu.wiki/w/%EB%8B%B9%EA%B5%AC?from=%ED%8F%AC%EC%BC%93%EB%B3%BC#s-3.1<br>
    댄스 스포츠: 살사, 탱고, 왈츠	https://namu.wiki/w/%EB%8C%84%EC%8A%A4%EC%8A%A4%ED%8F%AC%EC%B8%A0?from=%EB%8C%84%EC%8A%A4%20%EC%8A%A4%ED%8F%AC%EC%B8%A0<br>
    영화감상	https://namu.wiki/w/%EC%98%81%ED%99%94<br>
    음악 감상	https://namu.wiki/w/%EC%9D%8C%EC%95%85<br>
    연극	https://namu.wiki/w/%EC%97%B0%EA%B7%B9<br>
    뮤지컬 공연	https://namu.wiki/w/%EB%AE%A4%EC%A7%80%EC%BB%AC<br>
    음악공연	https://namu.wiki/w/%EC%9D%8C%EC%95%85<br>
    미술관	https://namu.wiki/w/%EB%B0%95%EB%AC%BC%EA%B4%80?from=%EB%AF%B8%EC%88%A0%EA%B4%80<br>
    박물관	https://namu.wiki/w/%EB%B0%95%EB%AC%BC%EA%B4%80?from=%EB%AF%B8%EC%88%A0%EA%B4%80<br>
    독서	https://namu.wiki/w/%EB%8F%85%EC%84%9C<br>
    한지공예	https://namu.wiki/w/%ED%95%9C%EC%A7%80<br>
    목공예	https://namu.wiki/w/%EB%B6%84%EB%A5%98:%EB%AA%A9%EA%B3%B5%EC%98%88<br>
    도자기 공예	https://namu.wiki/w/%EB%8F%84%EC%9E%90%EA%B8%B0<br>
    가죽 공예	https://namu.wiki/w/%EA%B0%80%EC%A3%BD<br>
    지점토	https://namu.wiki/w/%EC%A7%80%EC%A0%90%ED%86%A0<br>
    가구 만들기	https://namu.wiki/w/%EA%B0%80%EA%B5%AC<br>
    비누 공예	https://namu.wiki/w/%EA%B3%B5%EC%98%88<br>
    십자수	https://namu.wiki/w/%EC%8B%AD%EC%9E%90%EC%88%98<br>
    유리공예	https://namu.wiki/w/%EC%9C%A0%EB%A6%AC<br>
    리본 공예	https://namu.wiki/w/%EB%A6%AC%EB%B3%B8<br>
    와이어 공예	https://namu.wiki/w/%EC%99%80%EC%9D%B4%EC%96%B4<br>
    자수	https://namu.wiki/w/%EC%9E%90%EC%88%98<br>
    종이접기	https://namu.wiki/w/%EC%A2%85%EC%9D%B4%EC%A0%91%EA%B8%B0<br>
    스탬프 공예	https://namu.wiki/w/%EC%8A%A4%ED%83%AC%ED%94%84?noredirect=1<br>
    풍선 아트	https://namu.wiki/w/%ED%92%8D%EC%84%A0<br>
    팔찌 만들기	https://namu.wiki/w/%ED%8C%94%EC%B0%8C<br>
    인형 만들기	https://namu.wiki/w/%EC%9D%B8%ED%98%95<br>
    양초 공예	https://namu.wiki/w/%EC%96%91%EC%B4%88<br>
    꽃꽂이	https://namu.wiki/w/%EA%BD%83%EA%BD%82%EC%9D%B4<br>
    설탕 공예	https://namu.wiki/w/%EC%95%84%EB%A9%94%EC%9E%90%EC%9D%B4%EC%BF%A0?from=%EC%84%A4%ED%83%95%EA%B3%B5%EC%98%88<br>
    뜨개질	https://namu.wiki/w/%EB%9C%A8%EA%B0%9C%EC%A7%88<br>
    한식	https://namu.wiki/w/%ED%95%9C%EC%8B%9D<br>
    중식	https://namu.wiki/w/%EC%A4%91%EC%8B%9D<br>
    술 안주 요리	https://namu.wiki/w/%EC%88%A0%EC%95%88%EC%A3%BC<br>
    일식	https://namu.wiki/w/%EC%9D%BC%EC%8B%9D<br>
    양식	https://namu.wiki/w/%EC%96%91%EC%8B%9D<br>
    제과.제빵	https://namu.wiki/w/%EC%A0%9C%EB%B9%B5%EC%82%AC<br>
    외국어 공부	https://namu.wiki/w/%EC%99%B8%EA%B5%AD%EC%96%B4<br>
    수화공부	https://namu.wiki/w/%EC%88%98%ED%99%94<br>
    한문 공부	https://namu.wiki/w/%ED%95%9C%EB%AC%B8<br>
    수학 공부	https://namu.wiki/w/%EC%88%98%ED%95%99<br>
    애완동물	https://namu.wiki/w/%EC%95%A0%EC%99%84%EB%8F%99%EB%AC%BC<br>
    식물 키우기	https://namu.wiki/w/%EC%8B%9D%EB%AC%BC<br>
    컴퓨터 게임	https://namu.wiki/w/PC%20%EA%B2%8C%EC%9D%B4%EB%B0%8D?from=%EC%BB%B4%ED%93%A8%ED%84%B0%20%EA%B2%8C%EC%9E%84<br>
    유튜브 시청	https://namu.wiki/w/%EC%9C%A0%ED%8A%9C%EB%B8%8C<br>
    보드게임	https://namu.wiki/w/%EB%B3%B4%EB%93%9C%20%EA%B2%8C%EC%9E%84?from=%EB%B3%B4%EB%93%9C%EA%B2%8C%EC%9E%84<br>
    기타	https://namu.wiki/w/%EA%B8%B0%ED%83%80<br>
    바이올린	https://namu.wiki/w/%EB%B0%94%EC%9D%B4%EC%98%AC%EB%A6%B0<br>
    피아노	https://namu.wiki/w/%ED%94%BC%EC%95%84%EB%85%B8<br>
    드럼	https://namu.wiki/w/%EB%93%9C%EB%9F%BC<br>
  </p>
</div>
'''

script.printHtml(desc)
