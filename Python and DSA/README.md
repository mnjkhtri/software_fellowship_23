## SETUP GUIDE FOR RISE
1. install rise library
``` pip install rise```
2. install nbextensions
``` pip3 install jupyter_contrib_nbextensions```
```jupyter contrib nbextension install --user```
3. Add following to the file[if doesn't exist, make it]  `.jupyter/nbconfig/rise.json`:
```json
{

  "transition": "slide",
  "start_slideshow_at": "selected",
  "overlay": "<div class='myheader'></div>",
  "header": "<h1>Hello</h1>",
  "footer": "<h3>World!</h3>"
}
```
4. Update rise.css with following:
```css
.myheader{
    height: 100vh;
    background-image: url("bg.png");
    background-size: cover;
}
```
5. Enjoy!
