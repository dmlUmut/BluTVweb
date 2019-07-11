Getting Started with Gauge
==========================

This is an executable specification file. This file follows markdown syntax. Every heading in this file denotes a scenario. Every bulleted point denotes a step.
To execute this specification, use `mvn test`

İlk giriş sayfası kontrolü
---------------
*Yeni üye alanını kontrol et
*BarMenü alanını kontrol et
*FooterMenü alanını kontrol et

Yeni üye e-posta hatası kontrolü
---------------
*"Test Isim" üye ismini yaz
*"dml.umut@hotmail.com" üye mailini yaz
*"Test123456" üye şifresini yaz
*Eposta hata popupını kontrol et

Yeni üye eposta popup kontrolü
---------------
*"Test Isim" üye ismini yaz
*"dml.umut@" üye mailini yaz
*Eposta popupını kontrol et

Yeni üye şifre alanını kontrolü
---------------
*"Test Isim" üye ismini yaz
*"dml.umut@hotmail.com" üye mailini yaz
*"1234" üye şifresini yaz
*"btnRegister" elementine tıkla
*"10" saniye bekle
/*"popupEksikKarakter" elementi var mı
*"56" üye şifresini yaz
*"10" saniye bekle
/*"popupSifrenizHata" elementi var mı
*"d" üye şifresini yaz