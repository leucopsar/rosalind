def ins_sort(a, n):
    s = 0
    for i in range(1, n):
        k = i
        while k >= 1 and a[k] < a[k-1]:
            s += 1
            t = a[k-1]
            a[k-1]=a[k]
            a[k]=t
            k -= 1
    return (s, a)



n = "-12731 13332 65103 7627 29063 97552 88243 -87942 1016 54428 33456 96394 53371 50195 -82165 74396 -6699 -92056 -68745 74635 -41070 35957 24932 17267 -28118 -66992 -14365 61741 -45046 -12724 85765 -96265 10796 21398 -91974 18926 -90416 -85745 37925 18059 -8236 -99444 -37124 13128 57239 61934 66865 -92552 -70330 -60338 -5203 -72761 -580 3057 -8605 -11202 90451 -89785 51799 80342 7629 55236 44335 -48603 99393 20228 -6195 -80730 23516 31633 -73210 -72114 15786 -61547 64230 -87236 -92113 -23668 -156 -48201 37793 34716 89352 -57558 -84898 60806 -19444 62542 58019 24938 13464 -22827 -55372 -10365 16875 -33297 90795 -1994 -65559 4533 34898 -14326 -36436 -10179 -59196 -37 92155 22352 20984 -22498 -83272 -35047 -381 36255 48540 80476 31581 -88271 -72608 -75735 49268 14415 65999 -88625 95731 50792 36813 -92740 -45439 -20607 93218 46387 -15561 98001 -2789 -80731 50430 886 37747 -17515 -57989 58528 20524 -42549 78463 -96575 -81453 -32072 -76959 39506 -74311 61986 48760 -27208 90877 53535 52744 43349 53614 -8320 -54511 -17291 -73591 -23394 78191 26317 -71518 998 69689 -6106 -75971 -5024 -93488 99950 -88929 95515 16798 35049 12402 79887 50463 99560 -1190 42337 -97125 -59982 -54163 -45581 12914 37405 44084 20182 83960 23635 35456 -85758 -19362 96823 -87771 87258 47525 4231 -88428 1249 83007 -23792 70305 -59049 62329 20990 -70655 85759 -75848 55314 57954 49287 15054 27433 59383 6377 -42018 -76041 72221 -82206 -99270 31626 -24317 -74530 55497 67403 52098 -53273 23372 -82483 70369 -20147 99999 36377 99205 8840 -11583 72961 -73287 23149 -80034 93605 -20767 57838 14403 -20565 59674 -24115 -35895 -85878 91748 57717 -22746 -68729 94123 -68432 38626 71858 14599 53732 99854 79982 -45432 -12148 -11327 -39404 45571 45329 56782 63912 37051 53640 -96572 30421 79093 -22838 26279 -54784 -41846 13025 -94424 32237 -14122 61290 -75742 10168 1700 -37710 54867 96847 84210 -20972 -82478 -55330 68622 34208 64522 -64396 55648 -66076 98459 -2152 -53924 -4377 -1878 -24577 58642 -26756 -1088 32671 12966 13316 82121 -88211 -59422 -33815 68943 -55511 -25728 90244 -76216 65986 4268 37039 98061 -93557 -14342 -96686 15934 94306 -8280 66689 46612 18089 -3272 -34011 54933 1591 -4230 -50558 -58724 -13716 26598 40102 85043 -69848 82039 97275 -32380 -13490 -69698 -63065 91527 83448 -64917 98401 88995 45782 -69849 -88326 65133 -72622 -30047 -38709 -41941 -43263 22010 -81853 -63560 -28823 -26544 -42586 -27924 -39962 75361 82901 78206 -76648 -99361 76165 -76980 -83747 -50634 46920 43019 -87645 -35656 60592 17314 49134 -22730 -48154 -97727 -60007 8556 40022 96089 -65668 16133 84143 -18163 -3131 -96624 -62039 43556 -33811 -53006 -99046 -30534 25690 5215 -21586 -92951 23319 -78756 56040 -34867 -14455 61572 81856 84778 11774 60257 -14861 98622 30677 -96446 -13237 -3771 -28429 7608 82736 -32369 43660 -10189 19227 55818 -66378 27732 -15018 -89031 38673 95947 74411 11432 -95917 67665 64893 77156 76340 98674 -17494 -95558 76671 -47427 -80541 98628 -86591 35013 28896 -11205 16873 -7056 68854 -46712 75714 32910 -15769 89481 39801 38299 21240 69456 60198 -15291 -71508 55912 37209 63251 -48676 71847 16476 -9411 15963 46450 -4594 37099 71538 -93407 95210 14537 26031 -77921 -58618 -26267 -93402 -48258 -83139 51525 38859 -72002 -29479 -92436 -68655 -85943 51727 -24655 -24562 59738 74865 83880 -2810 -18339 78127 -38398 66199 -30479 -28040 -75087 21908 -90946 -76485 -27956 44758 85673 33678 20737 17688 -25897 -41652 27867 -28360 -83773 -61553 -67669 -23029 91938 -10806 -37907 56832 49577 -53756 -19042 63726 43094 19656 5505 88393 -97907 -58250 82145 -29895 41473 -45334 -60449 -28247 1544 -3161 -64290 -84336 -37409 5942 -55753 -99915 18609 -16571 4470 -6711 -73342 -48325 30619 37881 51867 -76490 -22127 -19405 86209 -61621 -40478 3266 -18256 78007 -96414 -49351 -93601 -74926 -37054 -51948 97546 7503 49835 90984 -9800 -33634 -6779 73098 92284 62547 80 63838 96933 -46423 -27546 -27449 -6072 15661 48546 -30323 98333 -19586 -74500 -10362 94208 51689 87984 -18470 90287 -14543 13910 -68724 75272 -87718 35972 34102 -12252 -12961 -71168 91791 44587 99796 60839 59163 40319 -24453 10291 3809 16061 4091 44836 -29974 22176 -56724 78013 43891 40914 -32672 80465 -75954 -71897 79901 91728 58192 65847 -77273 76035 -72960 66238 -46104 36931 32878 -12200 -88428 -68558 11164 -69435 32830 97483 -28809 -89607 -67785 -25831 3247 -51449 -66413 -35962 -48485 45258 -15898 56740 35244 27385 25080 97198 -19674 31917 21596 -99244 -14012 -29398 -12925 66996 -2713 70061 9445 -1685 -71269 -90531 65716 -60468 -87282 -58960 -35430 -13204 70062 -59407 -23613 -70240 94331 -39513 79755 -93347 10452 -1036 81156 -84943 2497 63663 -50982 82465 96358 45872 83417 64056 42798 -64077 -33974 28479 51142 -92685 3610 60617 -54344 43823 35219 -17459 39819 1670 96111 16776 -18558 7222 40150 -6148 -14251 -60220 -18603 31249 8258 -18225 -31681 20369 -60736 4669 -55193 -59532 49782 -17347 71611 -73054 22597 -11143 53870 14004 -7724 13503 -81709 -53641 -61601 14801 -96015 73677 -72004 70329 93221 57186 -33361 27001 -45240 -99169 89281 74987 -48972 84576 22838 -37684 -74616 -27257 16566 14268 -582 -4130 -22894 32515 64932 66010 -75939 -89515 -72008 -70277 56328 -11236 20905 -89919 -63317 12684 98463 -76595 75062 33666 -38510 49831 74335 -85845 3636 60864 -6352 31652 10881 39188 73328 72295 -29880 43295 -17722 85096 -85977 -53561 -6600 32717 -95842 -39743 -85815 69414 -17246 87740 -98902 40992 76696 32932 34918 -46146 85647 79822 37988 75326 55952 16023 -82632 58356 31543 76999 -20425 39127 94021 -33182 43215 41861 5421 -96966 -95600 -94955 -51765 44117 -45693 19495 14167 62448 85754 12143 -60300 39173 -81775 27876 -25396 54289 -60252 22365 49438 -36922 42089 70864 95900 59970 -30664 -14204 771 31018 -63566 37550 -45632 -64957 5817 25936 6334 -99219 -36350 91174 -17303 49839 24900 -13449 30340 90310 -38055 -39373 -23800 2863 80090 73856 48857 36953 21267 -9139 65919 81247 94801 -30323 -83586 -48017 54273 -81475 75098 -45044 -44553 48116 70889 19659 -97197 58929"
l = n.split(" ")
print(len(l))
l = [6,10,4,5,1,2]
print(ins_sort(l, len(l)))
