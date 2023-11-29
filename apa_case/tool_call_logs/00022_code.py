"""Function param descriptions: 
This function doesn't need params

This function has been executed for 1 times. Last execution:
1.Status: TriggerAcivatedSuccess
2.Input: 
[]

3.Output:
[{}]
"""
def trigger_0():
  """
  comments: 当用户手动触发时，启动工作流程
  TODOs: 
    - 实现触发器的参数设置
  """
  params = {}
  function = transparent_trigger(integration="manualTrigger", resource="default", operation="default")
  return function.run(input_data=None, params=params)



"""Function param descriptions: 
0 params["documentId"]: dict{"mode":enum(str),"values":any} = {'mode': 'list', 'value': ''}, Required: Document . "mode" should be one of ['url', 'id']: 
  0.0 params["documentId"]["value"](when "mode"="url"): string: By URL
  0.1 params["documentId"]["value"](when "mode"="id"): string: By ID
1 params["sheetName"]: dict{"mode":enum(str),"values":any} = {'mode': 'list', 'value': ''}, Required: Sheet . "mode" should be one of ['url', 'id']: 
  1.0 params["sheetName"]["value"](when "mode"="url"): string: By URL
  1.1 params["sheetName"]["value"](when "mode"="id"): string: By ID
2 params["filtersUI"]: dict[str,list[dict[str,any]]] = {}: Filters(Add Filter) . properties description:
  ...hidden...
3 params["options"]: dict = {}: Options(Add Option) . properties description:
  ...hidden...

This function has been executed for 1 times. Last execution:
1.Status: FunctionExecuteSuccess
2.Input: 
[{}]

3.Output:
[{'json': {'row_number': 2, 'Business Line': 3, 'Manager': 'blitherboom812@gmail.com', 'cost': 20000, 'sales': 10000, 'Description': 'Online Travel Booking Portal: Offering a comprehensive platform for consumers to book flights, hotels, and other travel-related services conveniently.', 'col_6': '', 'col_7': '', 'col_8': '', 'col_9': '', 'col_10': '', 'col_11': '', 'col_12': '', 'col_13': 20000, 'col_14': 10000, 'col_15': 'Online Travel Booking Portal: Offering a comprehensive platform for consumers to book flights, hotels, and other travel-related services conveniently.', 'col_16': 3, 'col_17': 'blitherboom812@gmail.com', 'col_18': 20000, 'col_19': 10000, 'col_20': 'Online Travel Booking Portal: Offering a comprehensive platform for consumers to book flights, hotels, and other travel-related services conveniently.', 'col_21': 3, 'col_22': 'blitherboom812@gmail.com', 'col_23': 20000, 'col_24': 10000, 'col_25': 'Online Travel Booking Portal: Offering a comprehensive platform for consumers to book flights, hotels, and other travel-related services conveniently.'}, 'pairedItem': {'item': 0}}]
"""
def action_0(input_data: List[Dict] =  [{...}]):
  """
  comments: 从Google Sheets中读取业务流数据，其中documentId和sheetName都是通过URL给出的。
  TODOs: 
    - 测试此功能
  """
  params = {
             "documentId": {
               "mode": "url",
               "value": "https://docs.google.com/spreadsheets/d/1_B038J1f3VW94z179OagFwEtnr3k5mTyXKBTPI2Fw-U/edit#gid=1759497495"
             },
             "sheetName": {
               "mode": "url",
               "value": "https://docs.google.com/spreadsheets/d/1_B038J1f3VW94z179OagFwEtnr3k5mTyXKBTPI2Fw-U/edit#gid=1759497495"
             }
           }
  function = transparent_action(integration="googleSheets", resource="sheet", operation="read")
  return function.run(input_data=input_data, params=params)



"""Function param descriptions: 
0 params["select"]: enum[string] = "", Required: Send Message To(Select...) . Available values:
  0.0 value=="channel": Channel
  0.1 value=="user": User
1 params["channelId"]: dict{"mode":enum(str),"values":any} = {'mode': 'list', 'value': ''}, Required: Channel. The Slack channel to send to(Select a channel...) . "mode" should be one of ['id', 'name', 'url']: 
  1.0 params["channelId"]["value"](when "mode"="id"): string: By ID(C0122KQ70S7E)
  1.1 params["channelId"]["value"](when "mode"="name"): string: By Name(#general)
  1.2 params["channelId"]["value"](when "mode"="url"): string: By URL(https://app.slack.com/client/TS9594PZK/B0556F47Z3A)
2 params["user"]: dict{"mode":enum(str),"values":any} = {'mode': 'list', 'value': ''}: User(Select a user...) . "mode" should be one of ['id', 'username']: 
  ...hidden...
3 params["messageType"]: enum[string] = "text": Message Type. Whether to send a simple text message, or use Slack’s Blocks UI builder for more sophisticated messages that include form fields, sections and more . Available values:
  3.0 value=="text": Simple Text Message. Supports basic Markdown
  3.1 value=="block": Blocks. Combine text, buttons, form elements, dividers and more in Slack 's visual builder
  3.2 value=="attachment": Attachments
4 params["text"]: string = "": Notification Text. Fallback text to display in slack notifications. Supports <a href="https://api.slack.com/reference/surfaces/formatting">markdown</a> by default - this can be disabled in "Options".
5 params["blocksUi"]: string = "", Required: Blocks. Enter the JSON output from Slack's visual Block Kit Builder here. You can then use expressions to add variable content to your blocks. To create blocks, use <a target='_blank' href='https://app.slack.com/block-kit-builder'>Slack's Block Kit Builder</a>
6 params["attachments"]: list[dict] = [{}]: Attachments(Add attachment item) . properties description:
  ...hidden...
7 params["otherOptions"]: dict = {}: Options. Other options to set(Add options) . properties description:
  ...hidden...

This function has been executed for 0 times. Last execution:
1.Status: DidNotBeenCalled
2.Input: 
[]

3.Output:
[]
"""
def action_1(input_data: List[Dict] =  [{...}]):
  """
  comments: 向Slack的#general频道发送消息
  TODOs: 
    - 测试此功能
  """
  params = {
             "select": "channel",
             "channelId": {
               "mode": "name",
               "value": "#general"
             }
           }
  function = transparent_action(integration="slack", resource="message", operation="post")
  return function.run(input_data=input_data, params=params)



"""Function param descriptions: 
0 params["sendTo"]: string = "", Required: To. The email addresses of the recipients. Multiple addresses can be separated by a comma. e.g. jay@getsby.com, jon@smith.com.(info@example.com)
1 params["subject"]: string = "", Required: Subject(Hello World!)
2 params["emailType"]: enum[string] = "text", Required: Email Type  You can't use expression.. Available values:
  2.0 value=="text": Text
  2.1 value=="html": HTML
3 params["message"]: string = "", Required: Message
4 params["options"]: dict = {}: Options(Add Option) . properties description:
  ...hidden...

This function has been executed for 0 times. Last execution:
1.Status: DidNotBeenCalled
2.Input: 
[]

3.Output:
[]
"""
def action_2(input_data: List[Dict] =  [{...}]):
  """
  comments: 向Gmail发送邮件，邮件的收件人、主题和内容都是通过输入数据给出的。
  TODOs: 
    - 测试此功能
  """
  params = {
             "sendTo": "={{$json['sendTo']}}",
             "subject": "={{$json['subject']}}",
             "message": "={{$json['message']}}"
           }
  function = transparent_action(integration="gmail", resource="message", operation="send")
  return function.run(input_data=input_data, params=params)



"""Function param descriptions: 
0 params["messages"]: string = "", Required: messages. Set system and user prompts here. An Example:{"messages": [{"role": "system","content": "Please say hello to user."}, {"role": "user","content": "Hello!"}]}

This function has been executed for 2 times. Last execution:
1.Status: FunctionExecuteSuccess
2.Input: 
[{'json': {'messages': [{'role': 'user', 'content': '业务流3的利润为-10000请给客户经理写一封邮件。'}], 'operation': 'default', 'resource': 'default'}}]

3.Output:
[{'json': {'choices': [{'text': '首先，我们需要定义一个函数来发送邮件。这个函数需要集成邮件服务（例如Gmail或Outlook），并且需要输入参数如收件人地址，邮件主题和邮件内容。在邮件内容中，我们将包含业务流3的利润信息。\n\n然后，我们将在工作流中调用这个函数，输入客户经理的邮件地址，邮件的主题和内容。邮件的内容将包含业务流3的利润信息。 \n\n具体实施如下：'}]}, 'pairedItem': {'item': 0}}]
"""
def action_3(input_data: List[Dict] =  [{...}]):
  """
  comments: 使用AI生成邮件内容
  TODOs: 
    - 实现动作的参数设置
  """
  params = {}  # to be Implemented
  function = transparent_action(integration="aiCompletion", resource="default", operation="default")
  return function.run(input_data=input_data, params=params)



"""

This function has been executed for 1 times. Last execution:
1.Status: ErrorRaisedHere
2.Input: 
[{}]

3.Output:
[]
"""
def mainWorkflow(trigger_input: [{...}]):
  """
  comments: 当用户手动触发时，从Google Sheets中读取业务流数据，计算业务流的利润，并判断业务流的类型，给业务经理发送盈利或亏损信息。
  TODOs: 
    - 测试此工作流程
  """
  # 从Google Sheets中读取业务流数据
  business_flow_data = action_0(trigger_input)
  # 计算业务流的利润
  for data in business_flow_data:
    data['json']['profit'] = data['json']['sales'] - data['json']['cost']
  # 判断业务流的类型，并给业务经理发送盈利或亏损信息
  for data in business_flow_data:
    business_type = action_3([{'json': {'messages': [{'role': 'user', 'content': 'Please determine whether the following business flow belongs to to B(to Business) or to C(to Client)? ' + data['json']['Description']}]}}])[0]['json']['choices'][0]['text']
    if 'to B' in business_type:
      # 如果业务流类型为to B，向Slack的#general频道发送消息
      message = {'json': {'text': '业务流' + str(data['json']['Business Line']) + '的利润为' + str(data['json']['profit'])}}
      action_1([message])
    elif 'to C' in business_type:
      # 如果业务流类型为to C，向该业务流经理发送一则提醒邮件
      message = {'json': {'messages': [{'role': 'user', 'content': '业务流' + str(data['json']['Business Line']) + '的利润为' + str(data['json']['profit']) + '请给客户经理写一封邮件。'}]}}
      email_content = action_3([message])
      email = {'json': {'sendTo': data['json']['manager'], 'subject': '业务流利润提醒', 'message': email_content[0]['json']['choices'][0]['text']}}
      action_2([email])
  return business_flow_data



"""

The directly running result for now codes with print results are as following:


Note: if there is 'KeyError' in the error message, it may be due to the wrong usage of output data. The output data info may help you: 
[Output Data Info]
the output data of function `trigger_0` is: `[{}]`
the output data of function `action_0` is: `[{'json': {'row_number': 2, 'Business Line': 3, 'Manager': 'blitherboom812@gmail.com', 'cost': 20000, 'sales': 10000, 'Description': 'Online Travel Booking Portal: Offering a comprehensive platform for consumers to book flights, hotels, and other travel-related services conveniently.', 'col_6': '', 'col_7': '', 'col_8': '', 'col_9': '', 'col_10': '', 'col_11': '', 'col_12': '', 'col_13': 20000, 'col_14': 10000, 'col_15': 'Online Travel Booking Portal: Offering a comprehensive platform for consumers to book flights, hotels, and other travel-related services conveniently.', 'col_16': 3, 'col_17': 'blitherboom812@gmail.com', 'col_18': 20000, 'col_19': 10000, 'col_20': 'Online Travel Booking Portal: Offering a comprehensive platform for consumers to book flights, hotels, and other travel-related services conveniently.', 'col_21': 3, 'col_22': 'blitherboom812@gmail.com', 'col_23': 20000, 'col_24': 10000, 'col_25': 'Online Travel Booking Portal: Offering a comprehensive platform for consumers to book flights, hotels, and other travel-related services conveniently.'}, 'pairedItem': {'item': 0}}]`
the output data of function `action_1` is: `[]`
the output data of function `action_2` is: `[]`
the output data of function `action_3` is: `[{'json': {'choices': [{'text': '首先，我们需要定义一个函数来发送邮件。这个函数需要集成邮件服务（例如Gmail或Outlook），并且需要输入参数如收件人地址，邮件主题和邮件内容。在邮件内容中，我们将包含业务流3的利润信息。\n\n然后，我们将在工作流中调用这个函数，输入客户经理的邮件地址，邮件的主题和内容。邮件的内容将包含业务流3的利润信息。 \n\n具体实施如下：'}]}, 'pairedItem': {'item': 0}}]`

------------------------
In Function: mainWorkflow
          email_content = action_3([message])
-->       email = {'json': {'sendTo': data['json']['manager'], 'subject': '业务流利润提醒', 'message': email_content[0]['json']['choices'][0]['text']}}
          action_2([email])
------------------------
KeyError: 'manager'

You can also see the runnning result for all functions in there comments.
"""