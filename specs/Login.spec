Getting Started with Gauge
==========================

This is an executable specification file. This file follows markdown syntax. Every heading in this file denotes a scenario. Every bulleted point denotes a step.
To execute this specification, use `mvn test`

Success Login Control
-----------
Tags: Success Login

*"dml.umut@hotmail.com" emaili ve "Deneme123" sifresi ile giris yap
*Doğru giriş yapıldı

Wrong Email Login Control
-------------
Tags: Wrong Email

*"dmlumut@hotmail.com" emaili ve "Deneme123" sifresi ile giris yap
*Giriş yapılamadı

Wrong Password Login Control
--------------
Tags: Wrong Password

*"dml.umut@hotmail.com" emaili ve "WrongPassword" sifresi ile giris yap
*Giriş yapılamadı

Remember Me Login Control
-------------
Tags: Remember Me Control

*Beni Hatırla butonunu kontrol et
*Çıkış yap

Create User Control
----------
Tags: New User

*Yeni kullanıcı oluşturma sayfasını kontrol et
*Yeni kullanıcı sayfası popuplarını kontrol et
*Yeni kullanıcı oluşturmayı kontrol et

Uyelik Sozlesmesi link kontrol
----------------
Tags: Link Control

*Yeni kullanıcı oluşturma sayfasını kontrol et
*Yeni kullanıcı popup link kontrolü

Session Ended Control
-----------
Tags: Session Control

*"dml.umut@hotmail.com" emaili ve "Deneme123" sifresi ile giris yap
*"3600" saniye bekle
*Oturum sonlandırma popupını kontrol et