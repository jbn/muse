------

```
   mmmmmmm    mmmmmmm    uuuuuu    uuuuuu       ssssssssss        eeeeeeeeeeee    
 mm:::::::m  m:::::::mm  u::::u    u::::u     ss::::::::::s     ee::::::::::::ee  
m::::::::::mm::::::::::m u::::u    u::::u   ss:::::::::::::s   e::::::eeeee:::::e
m::::::::::::::::::::::m u::::u    u::::u   s::::::ssss:::::s e::::::e     e::::e
m:::::mmm::::::mmm:::::m u::::u    u::::u    s:::::s  ssssss  e:::::::eeeee:::::e
m::::m   m::::m   m::::m u::::u    u::::u      s::::::s       e::::::::::::::::e 
m::::m   m::::m   m::::m u::::u    u::::u         s::::::s    e::::::eeeeeeeeee  
m::::m   m::::m   m::::m u:::::uuuu:::::u   ssssss   s:::::s  e:::::::e           
m::::m   m::::m   m::::m u:::::::::::::::uu s:::::ssss::::::s e::::::::e          
m::::m   m::::m   m::::m  u:::::::::::::::u s::::::::::::::s   e::::::::eeeeeeee  
m::::m   m::::m   m::::m   uu::::::::uu:::u  s:::::::::::ss     ee:::::::::::::e  
mmmmmm   mmmmmm   mmmmmm     uuuuuuuu  uuuu   sssssssssss         eeeeeeeeeeeeee  
```

------

Because, I was in a weird mood.

This uses `Flask` + `youtube_dl` to save vides as MP3 files. 

Scraped together in 20 minutes. Good luck.


# Install

```bash
brew install ffmpeg  # you probably have this
git clone https://github.com/jbn/muse.git
cd muse
pip install -r requirements.txt 
# Drag to your bookmark's bar. 
# You'll have to check "okay" for security somewhere each tab close.
# I need to fix this.
open bookmarket.html 

python muse.py  # Run the server

open http://localhost:1994  # Browse downloads
```
