<p align="center">
    <img src="./gambar-petunjuk/vecteezy_google-drive-icon-logo.png" alt="googledrive-icon" style="display: block; margin: 0 auto; width: 25%;">
</p>

# Google Services API oAuth 2.0 Authentication dengan python 2024

Accounts :
- email 	: sadeyanebabah.care@gmail.com
- console 	: https://console.developers.google.com/
- storage	: google drive ( Directories My Drive -> jakarta -> test-drive )
---

Akan melakukan penulisan file pada google drive dengan menggunakan oAuth 2.0 Authentication dari Google Services API.
Berikut tahapan-tahapan yang harus dilakukan :
---
<p align="left">Lakukan akses ke console cloud google.</p>
<p align="center">
    <img src="./gambar-petunjuk/ss_001.png" alt="001" style="display: block; margin: 0 auto;">
</p>

<p align="left">Membuat project.</p>
<p align="center">
    <img src="./gambar-petunjuk/ss_002.png" alt="002" style="display: block; margin: 0 auto;">
</p>
<p align="center">
    <img src="./gambar-petunjuk/ss_003.png" alt="003" style="display: block; margin: 0 auto;">
</p>
<p align="center">
    <img src="./gambar-petunjuk/ss_004.png" alt="004" style="display: block; margin: 0 auto;">
</p>

<p align="left">Enable Google Drive API.</p>
<p align="center">
    <img src="./gambar-petunjuk/ss_005.png" alt="005" style="display: block; margin: 0 auto;">
</p>
<p align="center">
    <img src="./gambar-petunjuk/ss_006.png" alt="006" style="display: block; margin: 0 auto;">
</p>
<p align="center">
    <img src="./gambar-petunjuk/ss_007.png" alt="007" style="display: block; margin: 0 auto;">
</p>

<p align="left">Membuat Credential OAuth 2.0 Client ID.</p>
<p align="center">
    <img src="./gambar-petunjuk/ss_008.png" alt="008" style="display: block; margin: 0 auto;">
</p>
<p align="center">
    <img src="./gambar-petunjuk/ss_009.png" alt="009" style="display: block; margin: 0 auto;">
</p>
<p align="center">
    <img src="./gambar-petunjuk/ss_010.png" alt="010" style="display: block; margin: 0 auto;">
</p>
<p align="center">
    <img src="./gambar-petunjuk/ss_011.png" alt="011" style="display: block; margin: 0 auto;">
</p>
<p align="center">
    <img src="./gambar-petunjuk/ss_012.png" alt="012" style="display: block; margin: 0 auto;">
</p>
<p align="center">
    <img src="./gambar-petunjuk/ss_013.png" alt="013" style="display: block; margin: 0 auto;">
</p>

### rename file credential hasi download tersebut :
    ❯ mv client_secret_1063147155563-pcrdp41ung33243jichsakah34o9b4ml.apps.googleusercontent.com.json client_secrets.json

    ❯ ls -lah | grep client_secrets
    -rw-r--r--   1 powercommerce  staff   407B Feb 18 15:14 client_secrets.json
<p align="left">Dapat dikonfersikan dengan https://jsonprettier.com agar json lebih mudah di baca.</p>
<p align="center">
    <img src="./gambar-petunjuk/jsonprettier.png" alt="jsonprettier" style="display: block; margin: 0 auto;">
</p>

<p align="center">
    <img src="./gambar-petunjuk/ss_014.png" alt="014" style="display: block; margin: 0 auto;">
</p>


