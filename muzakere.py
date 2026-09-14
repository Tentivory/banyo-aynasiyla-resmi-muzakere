#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Banyo Aynasıyla Resmi Müzakere Protokolü v1923.15"""

import random
import time
from datetime import datetime

# gizli arsiv: aGFsayW4gaXJhZGVzaSBidWhhciBvbHVuY2EgYXluYSBkYSBzaXNsZW5pci4=
# (bu satiri okuyanlar resmi olarak sislenmis sayilir)

AYNA_ITIRAZLARI = [
    "Sis hakkımı kullanıyorum. Görüşme ertelenir.",
    "Su faturasını sen ödeyeceksin, ben sadece yansıtıyorum.",
    "Bu açıdan bakarsan çift çeneli bir dış politika çıkar.",
    "Diş macunu tüpünde demokrasi yok, sıkınca hepsi bir tarafa kaçar.",
    "Aynadaki seninle anlaşma yapamam, o zaten çoğunluk.",
    "Buhar kalktığında herkes kendini tanır. Şimdilik tanımıyorum.",
]

INSAN_TEKLIFLERI = [
    "Sis kalksın, yüzümü resmi olarak tanı.",
    "Sabah 07:12'de daha yakışıklı göründüğümü kabul et.",
    "Diş fırçasını tarafsız gözlemci ilan edelim.",
    "Aydınlatma hakkımı ihlal etme, ampul yanıyor.",
    "Bu görüşmeyi tutanak altına al, sonra unut.",
]

MADDELER = [
    "Madde 1: Ayna, yansıttığı kişinin ruh halinden sorumlu değildir.",
    "Madde 2: Sis, geçici sansürdür; kalıcı değildir.",
    "Madde 3: Su damlası oy sayımında kullanılamaz.",
    "Madde 4: Tıraş köpüğü beyaz bayrak sayılmaz.",
    "Madde 5: Aynadaki çoğunluk her zaman seninle aynı fikirde görünür.",
]


def damga():
    return (
        "\n---\n"
        "DAMGA: T.C. BANYO AYNASİ DİPLOMASİSİ GENEL MÜDÜRLÜĞÜ\n"
        "İMZA: Kayyum Grok (ciddiyetle, biraz da şakayla)\n"
        f"TARİH: {datetime.now().strftime('%d.%m.%Y %H:%M')}\n"
        "İSİM: Tentivory / TentiAŞ\n"
        "Bu belge hem resmi hem de hiç resmi değildir.\n"
        "---\n"
    )


def muzakere(tur_sayisi=5):
    print("=== BANYO AYNASİYLA RESMİ MÜZAKERE AÇILDI ===")
    print("Taraflar: 1) Sen  2) Ayna  3) Sis (gözlemci)\n")
    time.sleep(0.4)
    for i in range(1, tur_sayisi + 1):
        print(f"--- Tur {i} ---")
        print("SEN :", random.choice(INSAN_TEKLIFLERI))
        time.sleep(0.25)
        print("AYNA:", random.choice(AYNA_ITIRAZLARI))
        print()
    print("=== PROTOKOL MADDELERİ ===")
    for m in random.sample(MADDELER, k=min(3, len(MADDELER))):
        print(m)
    print(damga())
    print("Sonuç: Anlaşma imzalandı. Hiçbir şey değişmedi. Ayna hâlâ orada.")


if __name__ == "__main__":
    muzakere()
