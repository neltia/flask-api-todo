# flask-api-todo
Flask-RESTX 라이브러리 활용 REST API 작성 예제, Todo API 작성

## 프로젝트 소개
- https://neltia.notion.site/41731b70f6da41f2aab39d2ca65f93e5?v=3be5b130c1724057842a383f7fc161b5
<p>
    엘라스틱서치 With Python을 주제로 사용해왔던 내용을 복습하며 정리합니다.
</p>
<p>
    오픈 소스 검색 엔진, ES(Elasticsearch)에 대한 기본 이론을 정리하면서 Python으로 ES에 질의하는 방법을 다룹니다. 나아가 Flask-RESTX 활용 API 구성과 Kibana를 통한 시각화까지 이뤄질 수 있도록 합니다.
<p>

## 개발 환경
virtualenv: Vagrantfile setup & Virtualbox
- vagrant: 2.4.0
- virtualbox: 6.1
- linux: ubuntu linux 22.04

lang: Python 3.10.6
lib.ver.
<pre>
python-dotenv==0.21.1
Flask==2.2.2
flask-restx==1.1.0
elastic-transport==8.10.0
elasticsearch==8.11.0
elasticsearch-dsl==8.11.0
</pre>

## 프로젝트 구성 방법
### Vagrant 환경 구성
- refer. <a href="https://blog.naver.com/dsz08082/223246524752">Vagrant/VirtualBox 환경에서 엘라스틱서치 및 키바나 8.10 설치</a>
- vagrant install: https://developer.hashicorp.com/vagrant/install?product_intent=vagrant
- virtualbox install: https://www.virtualbox.org/wiki/Download_Old_Builds_6_1
<p>
    vagrant: Virtualbox 등 가상화 소프트웨어를 CUI 환경에서 자동화할 수 있도록 돕는 도구.
</p>
<p>
    Vagrantfile만 가지고 명령어를 입력하면 로컬 환경에서 공통된 환경을 사용할 수 있음
</p>
<p>
    우분투 이미지 다운로드, 포트포워딩, 메모리 및 CPU 설정이 작성된 vagrant 파일이 있는 위치에서 up 명령어로 이미지를 다운로드 받아 실행
</p>
<pre>
    vagrant up
    vagrant ssh
</pre>

### Elasticsearch & Kibana 설치
<strong>Elasticsearch install</strong>
- elasticsearch serivce install
<pre>
sudo -i
wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo gpg --dearmor -o /usr/share/keyrings/elasticsearch-keyring.gpg
sudo apt-get install apt-transport-https
echo "deb [signed-by=/usr/share/keyrings/elasticsearch-keyring.gpg] https://artifacts.elastic.co/packages/8.x/apt stable main" | sudo tee /etc/apt/sources.list.d/elastic-8.x.list
sudo apt-get update && sudo apt-get install elasticsearch
sudo service elasticsearch start
</pre>
- elasticsearch password setting
<pre>
/usr/share/elasticsearch/bin/elasticsearch-reset-password -u elastic -i
</pre>

<strong>Kibana install</strong>
- kibana service setting
<pre>
sudo apt-get update && sudo apt-get install kibana
</pre>
- kibana token setting
<pre>
/usr/share/kibana/bin/kibana-setup --enrollment-token $(/usr/share/elasticsearch/bin/elasticsearch-create-enrollment-token -s kibana)
</pre>
<pre>
- kibana host setting
server.host 주석 해제 및 "0.0.0.0"으로 수정
</pre>
vim /etc/kibana/kibana.yml
<pre>
- kibana boot
server.host 주석 해제 및 "0.0.0.0"으로 수정
</pre>
<pre>
sudo /bin/systemctl daemon-reload
sudo /bin/systemctl enable kibana.service
sudo systemctl restart kibana.servic
</pre>

### project setup
라이브러리 설치
<pre>
pip install -r requirement.txt
</pre>

Elasticsearch CA File copy (Vagrant SSH)
- /vagrant 디렉터리에 파일을 복사하면 Vagrantfile이 있는 곳에 파일이 복사됨
<pre>
cp /etc/elasticsearch/certs/https_ca.crt /vagrant
</pre>

.env 환경변수 파일 작성
<pre>
FLASK_APP=manage.py
FLASK_DEBUG=development
ES_API_KEY=...
ES_HOST=localhost
ES_PORT=9200
ES_CRT_PATH=http_ca.crt
</pre>

- 테스트 서버 파일 실행
<pre>
python manage.py
</pre>
