import requests
import json
import jsonpath

def get_response(session,HOSTS,APPID,SECRET,grant_type='client_credential'):
    grant_dict={
        'grant_type':grant_type,
        'appid':APPID,
        'secret':SECRET
    }
    response = session.get(
        url='https://%s/cgi-bin/token'% HOSTS,
            params=grant_dict )
 #   print(response)
    # self.body = self.response.content.decode('utf-8')
    # 打印token
    return response

def get_token(session,HOSTS,APPID,SECRET):
    response = get_response(session,HOSTS,APPID,SECRET)
    access_token = response.json()['access_token']
  #  print('token获取值是：%s' % access_token)
    return access_token

def create_label(session,HOSTS,APPID,SECRET,createlabel_name):
    access_token = get_token(session, HOSTS, APPID, SECRET)
    param_data = {'access_token': access_token}
    json_data = {"tag": {"name": createlabel_name}}
    #当ensure_ascii是false的时候，可以返回ASCII码的值，否则就会被JSON转义
    new_data = json.dumps(json_data,ensure_ascii=False)
    #post中字典传值json，字符串传值data
    response_add = requests.post(url='https://%s/cgi-bin/tags/create' % HOSTS,
                                 params=param_data,
                                 data=new_data.encode('utf-8')
                                 )
   # body_add = response_add.content.decode('utf-8')
    return response_add

#查询第一个标签的标签名，进行成功判断
def select_label(session,HOSTS,APPID,SECRET):
    access_token = get_token(session, HOSTS, APPID, SECRET)
    param_data = {'access_token': access_token}
    response_select = session.get(url='https://%s/cgi-bin/tags/get' % HOSTS,
                                             params=param_data)
    return response_select

#修改第2个标签
def revise_label(session,HOSTS,APPID,SECRET,reviselabel_name,response_select):
    access_token = get_token(session, HOSTS, APPID, SECRET)
    param_data = {'access_token': access_token}
    #需要将查询的标签结果response_select转码，转码后str类型
    body_select = response_select.content.decode('utf-8')
    id_value = json.loads(body_select)
    id_revise = jsonpath.jsonpath(id_value, '$.tags[1].id')[0]
    json_revise = {"tag": {"id": id_revise, "name":reviselabel_name}}
    data_revise = json.dumps(json_revise,ensure_ascii=False)
    print(data_revise)
    response_revise = session.post(url='https://%s/cgi-bin/tags/update' %HOSTS,
                                         params=param_data,
                                         data=data_revise.encode('utf-8'))
    return response_revise

#删除第3个标签
def delete_label(session,HOSTS,APPID,SECRET,response_select):
    access_token = get_token(session, HOSTS, APPID, SECRET)
    param_data = {'access_token': access_token}
    #需要将查询的标签结果response_select转码，转码后str类型
    body_select = response_select.content.decode('utf-8')
    id_value = json.loads(body_select)
    id_delete = jsonpath.jsonpath(id_value, '$.tags[2].id')[0]
    json_delete = {"tag": {"id": id_delete}}
    response_delete = requests.post(url='https://%s/cgi-bin/tags/delete' % HOSTS,
                                    params=param_data,
                                    json=json_delete)
    return response_delete

