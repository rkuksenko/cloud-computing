MAIN_PAGE = '''
<style>
    #api_table {
      font-family: "Trebuchet MS", Arial, Helvetica, sans-serif;
      border-collapse: collapse;
      width: 100%;
    }
    
    #api_table td, #api_table th {
      border: 1px solid #ddd;
      padding: 8px;
    }
    
    #api_table tr:nth-child(even){background-color: #f2f2f2;}
    
    #api_table tr:hover {background-color: #ddd;}
    
    #api_table th {
      padding-top: 12px;
      padding-bottom: 12px;
      text-align: left;
      background-color: #4CAF50;
      color: white;
    }

  </style>
<body style="background-color:#CECECE;">
  <h1>Hello Oleksandr Korochkin!</h1>
  <hr>
  <p>The modulation of cloud computing using API requests. You may create a task with different weights (time of execution) and see real-time task execution. All tasks created in separate threads.</p>
  <p>To see this page use <a href="http://35.238.215.222"><b>http://35.238.215.222</b></a></p>
  <p>To see amount of active threads (tasks) use <a href="http://35.238.215.222/get-active-tasks-count"><b>http://35.238.215.222/get-active-tasks-count</b></a></p>
  <p>To see all created tasks use <a href="http://35.238.215.222/get-all-tasks"><b>http://35.238.215.222/get-all-tasks</b></a></p>
  <p>To add task use POST request on <b>http://35.238.215.222/push-task-with-weight/$weight$</b> where weight is an execution time.<br>
  The easyest way to make POST request - use preconfigured <a href="https://apitester.com/shared/checks/1ec6b2395e7645668aa8dc7fb2b5960d">apitester.com</a> (Don't forget to specify weight)<br>
  Also you may use simple curl request like this: "curl "http://35.238.215.222/push-task-with-weight/12" -X POST"</p>
  <hr>
  <p>Here is a list of supported API:<p>

  <div style="background-color:white;">
    <table id="api_table">
      <tr>
        <th>API URI</th>
        <th>HTTP Method</th>
        <th>Description</th>
      </tr>
      <tr>
        <td>/get-active-tasks-count</td>
        <td>GET</td>
        <td>Returns active tasks count</td>
      </tr>
      <tr>
        <td>"/"</td>
        <td>GET</td>
        <td>Returns this info</td>
        </tr>
      <tr>
        <td>/get-all-tasks</td>
        <td>GET</td>
        <td>Returns all tasks, both active and finished</td>
      </tr>
      <tr>
        <td>/push-task-with-weight/$weight$</td>
        <td>POST</td>
        <td>Create a task with some weight. "weight" - task execution duration in seconds</td>
      </tr>
    </table>
    </div>
    <p style="padding-top: 5%;">&copy; Created by Roman Kuksenko for subject "GRID - Technologies and Distributed Computing", 2020</p>
</body>
'''