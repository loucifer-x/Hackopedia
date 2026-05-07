## Document object model

<ins>**Possible vulnerable input**</ins>
*  innerHTML
*  outerHTML
*  document.write()
*  insertAdjacentHTML()
*  eval() / Function()
*  location, location.hash, location.search
*  v-html

<ins>**FINDING A VULNERABLE INPUT**</ins>




<ins>**EXAMPLE**</ins>
*Based on Vite app tryhackme challenge*

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
