#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2026
# study-geany.py
# 2026-06-25 2026-07-03 1.4

# ~ В данной папке есть файл homeinf.geany с информацией о редактируемых файлах,
# ~ ниже дано его содержание,
# ~ определить:
# ~ - сколько разделов в этом файле конфигурации,
# ~ - сколько файлов редактируется им?
# ~ - сколько из них питоновских?
# ~ какую версию питона испольузуем?

# ------------------------------------------------------

data = """
[editor]
line_wrapping=true
line_break_column=72
auto_continue_multiline=true

[file_prefs]
final_new_line=true
ensure_convert_new_lines=true
strip_trailing_spaces=false
replace_tabs=false

[indentation]
indent_width=4
indent_type=0
indent_hard_tab_width=8
detect_indent=false
detect_indent_width=false
indent_mode=2

[project]
name=homeinf
base_path=/home/edu
description=
file_patterns=

[long line marker]
long_line_behaviour=1
long_line_column=80

[files]
current_page=142
FILE_NAME_0=33327;Markdown;0;EUTF-8;0;1;1;%2Fhome%2Fedu%2Fhomeinf%2Ftodo.md;0;4
FILE_NAME_1=105;Python;0;EUTF-8;0;1;1;%2Fhome%2Fedu%2Fhomeinf%2Fnested_parens.py;0;4
FILE_NAME_2=22;Python;0;EUTF-8;0;1;1;%2Fhome%2Fedu%2Fhomeinf%2Fmany-zeros.py;0;4
FILE_NAME_3=473;Python;0;EUTF-8;0;1;1;%2Fhome%2Fedu%2Fhomeinf%2Flong-go-up.py;0;4
FILE_NAME_4=82;Python;0;EUTF-8;0;1;1;%2Fhome%2Fedu%2Fhomeinf%2Fnum-digits-listed.py;0;4
FILE_NAME_5=0;Python;0;EUTF-8;0;1;1;%2Fhome%2Fedu%2Fhomeinf%2Fnum-digits.py;0;4
FILE_NAME_6=417;Python;0;EUTF-8;0;1;1;%2Fhome%2Fedu%2Fhomeinf%2Fknignt-order-safe.py;0;4
FILE_NAME_7=231;Python;0;EUTF-8;0;1;1;%2Fhome%2Fedu%2Fhomeinf%2Fknignt-order-que.py;0;4
FILE_NAME_8=0;Python;0;EUTF-8;0;1;1;%2Fhome%2Fedu%2Fhomeinf%2Fknignt-order.py;0;4
FILE_NAME_9=0;Python;0;EUTF-8;0;1;1;%2Fhome%2Fedu%2Fhomeinf%2Fsort-extern.py;0;4
FILE_NAME_10=3032;Python;0;EUTF-8;0;1;1;%2Fhome%2Fedu%2Fhomeinf%2Fpaint-area-que.py;0;4
FILE_NAME_11=21;Python;0;EUTF-8;0;1;1;%2Fhome%2Fedu%2Fhomeinf%2Fpaint-area-rec.py;0;4
FILE_NAME_12=0;Python;0;EUTF-8;0;1;1;%2Fhome%2Fedu%2Fhomeinf%2Fcalc-expr.py;0;4
FILE_NAME_13=0;Markdown;0;EUTF-8;0;1;1;%2Fhome%2Fedu%2Fhomeinf%2Ftoc.md;0;4
FILE_NAME_14=0;Python;0;EUTF-8;0;1;1;%2Fhome%2Fedu%2Fhomeinf%2Fmax-three.py;0;4
FILE_NAME_15=1754;Python;0;EUTF-8;0;1;1;%2Fhome%2Fedu%2Fhomeinf%2Fmax-density.py;0;4
FILE_NAME_16=54;Python;0;EUTF-8;0;1;1;%2Fhome%2Fedu%2Fhomeinf%2Fnon-empty-lines.py;0;4
FILE_NAME_17=674;Python;0;EUTF-8;0;1;1;%2Fhome%2Fedu%2Ftests%2Ftypes%2Fself.py;0;4
FILE_NAME_18=888;Python;0;EUTF-8;0;1;1;%2Fhome%2Fedu%2Fhomeinf%2Fhas-ada.py;0;4
FILE_NAME_19=0;Python;0;EUTF-8;0;1;1;%2Fhome%2Fedu%2Fhomeinf%2Fsame-num-matrices.py;0;4
FILE_NAME_20=0;Python;0;EUTF-8;0;1;1;%2Fhome%2Fedu%2Fhomeinf%2Fdiff-digits.py;0;4
FILE_NAME_21=1064;Python;0;EUTF-8;0;1;1;%2Fhome%2Fedu%2Fhomeinf%2Fsuper-seven.py;0;4
FILE_NAME_22=0;Python;0;EUTF-8;0;1;1;%2Fhome%2Fedu%2Fhomeinf%2Fcube-4d.py;0;4
FILE_NAME_23=1118;Python;0;EUTF-8;0;1;1;%2Fhome%2Fedu%2Fhomeinf%2Ffind-vars-nostate.py;0;4
FILE_NAME_24=1180;Python;0;EUTF-8;0;1;1;%2Fhome%2Fedu%2Ftests%2Fmaze-maker2.py;0;4
FILE_NAME_25=307;Python;0;EUTF-8;0;1;1;%2Fhome%2Fedu%2Fhomeinf%2Farr-nums-op.py;0;4
FILE_NAME_26=0;Python;0;EUTF-8;0;1;1;%2Fhome%2Ftests%2Fpyetc%2Fmain.py;0;4
FILE_NAME_27=706;Python;0;EUTF-8;0;1;1;%2Fhome%2Fedu%2Fhomeinf%2Fgraph-exer.py;0;4
FILE_NAME_28=2882;Python;0;EUTF-8;0;1;1;%2Fhome%2Fedu%2Fhomeinf%2Fgraph-map.py;0;4
FILE_NAME_29=0;Python;0;EUTF-8;0;1;1;%2Fhome%2Fedu%2Fhomeinf%2Fgraph-que.py;1;4
FILE_NAME_30=1538;Python;0;EUTF-8;0;1;1;%2Fhome%2Fedu%2Fhomeinf%2Fplace-996.py;0;4
FILE_NAME_31=396;Python;0;EUTF-8;0;1;1;%2Fhome%2Fedu%2Fhomeinf%2Ffind-num-arr.py;0;4
FILE_NAME_32=434;Python;0;EUTF-8;0;1;1;%2Fhome%2FAIML%2FDS-OCR%2Ftest01.py;0;4
FILE_NAME_33=1845;Python;0;EUTF-8;0;1;1;%2Fhome%2Fedu%2Fhomeinf%2Ftree-oper-plus.py;0;4
FILE_NAME_34=541;Python;0;EUTF-8;0;1;1;%2Fhome%2FBogomaz%2F2025-11-30%2Fmain.py;0;4
FILE_NAME_35=527;Python;0;EUTF-8;0;1;1;%2Fhome%2FBogomaz%2Ftests%2Foutlines%2Fone.py;0;4
FILE_NAME_36=5568;Python;0;EUTF-8;0;1;1;%2Fhome%2FBogomaz%2F2025-12-15%2Ftest-3a.py;0;4
FILE_NAME_37=0;Python;0;EUTF-8;0;1;1;%2Fhome%2FBogomaz%2F2025-12-15%2Fprocess3.py;0;4
FILE_NAME_38=4363;Python;0;EUTF-8;0;1;1;%2Fhome%2FBogomaz%2F2025-12-15%2Ftest-3.py;0;4
FILE_NAME_39=452;Python;0;EUTF-8;0;1;1;%2Fhome%2Fedu%2Fhomeinf%2Fprimes%2Fsum-prod-primes-gen.py;0;4
FILE_NAME_40=1216;Python;0;EUTF-8;0;1;1;%2Fhome%2Fedu%2Fhomeinf%2Fprimes%2Fsum-prod-primes.py;0;4
FILE_NAME_41=0;Python;0;EUTF-8;0;1;1;%2Fhome%2Fedu%2Fhomeinf%2Fgraph-rec.py;0;4
FILE_NAME_42=698;Python;0;EUTF-8;0;1;1;%2Fhome%2Fedu%2Fhomeinf%2Fgraph-rec0.py;0;4
FILE_NAME_43=2080;Python;0;EUTF-8;0;1;1;%2Fhome%2FBogomaz%2Ftests%2Fover%2Ftest1.py;0;4
FILE_NAME_44=1615;Python;0;EUTF-8;0;1;1;%2Fhome%2Fmyke%2Fpvt%2FДенис%2F2026%2Fscatter1.py;0;4
FILE_NAME_45=17;None;0;EUTF-8;0;1;1;%2Fhome%2Fmyke%2Fpvt%2FДенис%2F2026%2Fdatap.tsv;0;4
FILE_NAME_46=1067;Python;0;EUTF-8;0;1;1;%2Fhome%2Fmyke%2Fpvt%2FДенис%2F2026%2Fmain.py;0;4
FILE_NAME_47=813;JSON;0;EUTF-8;0;1;1;%2Fhome%2Fmyke%2F.config%2Fopencode%2Fopencode.json;0;4
FILE_NAME_48=708;Python;0;EUTF-8;0;1;1;%2Fhome%2Fedu%2Fhomeinf%2Ftree-oper.py;0;4
FILE_NAME_49=0;Python;0;EUTF-8;0;1;1;%2Fhome%2Fedu%2Fhomeinf%2Fbest-flat.py;0;4
FILE_NAME_50=1999;Python;0;EUTF-8;0;1;1;%2Fhome%2Fedu%2Fhomeinf%2Ffind-vars-order.py;0;4
FILE_NAME_51=1886;Python;0;EUTF-8;0;1;1;%2Fhome%2Fedu%2Fhomeinf%2Ffind-vars-simple.py;0;4
FILE_NAME_52=838;Python;0;EUTF-8;0;1;1;%2Fhome%2Fedu%2Fhomeinf%2Fnumeral-systems.py;0;4
FILE_NAME_53=3050;Python;0;EUTF-8;0;1;1;%2Fhome%2Fedu%2Fhomeinf%2Fnumsys-convert.py;0;4
FILE_NAME_54=82;Python;0;EUTF-8;0;1;1;%2Fhome%2Fedu%2Fhomeinf%2Fsqeq.py;0;4
FILE_NAME_55=951;Python;0;EUTF-8;0;1;1;%2Fhome%2Fedu%2Fhomeinf%2Fsqeqc.py;0;4
FILE_NAME_56=0;Python;0;EUTF-8;0;1;1;%2Fhome%2Fpythoner%2Fqueens%2Fqueens26count.py;0;4
FILE_NAME_57=4002;Python;0;EUTF-8;0;1;1;%2Fhome%2Fedu%2Fhomeinf%2Fbad-habits.py;0;4
FILE_NAME_58=2315;Python;0;EUTF-8;0;1;1;%2Fhome%2Fedu%2Fhomeinf%2Fmy-bisect.py;0;4
FILE_NAME_59=41;Python;0;EUTF-8;0;1;1;%2Fhome%2Fedu%2Ftests%2Fquines%2Fquine1.py;0;4
FILE_NAME_60=4;Python;0;EUTF-8;0;1;1;%2Fhome%2Fedu%2Ftests%2Fquines%2Fquine2.py;0;4
FILE_NAME_61=86;Python;0;EUTF-8;0;1;1;%2Fhome%2Fedu%2Ftests%2Fquines%2Fquine3.py;0;4
FILE_NAME_62=79;Python;0;EUTF-8;0;1;1;%2Fhome%2Fedu%2Fhomeinf%2Fcode-phrase.py;0;4
FILE_NAME_63=2200;Python;0;EUTF-8;0;1;1;%2Fhome%2Fedu%2Fhomeinf%2Floop-stopper.py;0;4
FILE_NAME_64=1582;Python;0;EUTF-8;0;1;1;%2Fhome%2Fedu%2Fhomeinf%2Fyabeda.py;0;4
FILE_NAME_65=165;Python;0;EUTF-8;0;1;1;%2Fhome%2Fedu%2Ftests%2Fmatemagic%2Fplus.py;0;4
FILE_NAME_66=0;Python;0;EUTF-8;0;1;1;%2Fhome%2Fedu%2Fclasses%2Fstore-data.py;0;4
FILE_NAME_67=572;Python;0;EUTF-8;0;1;1;%2Fhome%2Fedu%2Fclasses%2Fvectors2.py;0;4
FILE_NAME_68=0;Python;0;EUTF-8;0;1;1;%2Fhome%2Fedu%2Fclasses%2Fvectors1.py;0;4
FILE_NAME_69=342;Python;0;EUTF-8;0;1;1;%2Fhome%2Fedu%2Fhomeinf%2Fmagic3.py;0;4
FILE_NAME_70=0;Python;0;EUTF-8;0;1;1;%2Fhome%2Fedu%2Fhomeinf%2Feo-line.py;0;4
FILE_NAME_71=246;Python;0;EUTF-8;0;1;1;%2Fhome%2Fwww%2Fbard-afisha-2026%2Fmain.py;0;4
FILE_NAME_72=167;Markdown;0;EUTF-8;0;1;1;%2Fhome%2Fedu%2FREADME.md;0;4
FILE_NAME_73=0;Python;0;EUTF-8;0;1;1;%2Fhome%2Fedu%2Fhomeinf%2Floop-words.py;0;4
FILE_NAME_74=321;Python;0;EUTF-8;0;1;1;%2Fhome%2Fedu%2Fhomeinf%2Fexbrace.py;0;4
FILE_NAME_75=0;Python;0;EUTF-8;0;1;1;%2Fhome%2Fedu%2Fhomeinf%2Flinearize.py;0;4
FILE_NAME_76=1380;Python;0;EUTF-8;0;1;1;%2Fhome%2Fedu%2Fhomeinf%2Fenums.py;0;4
FILE_NAME_77=0;Python;0;EUTF-8;0;1;1;%2Fhome%2Fedu%2Fhomeinf%2Fanagram2.py;0;4
FILE_NAME_78=0;Python;0;EUTF-8;0;1;1;%2Fhome%2Fedu%2Fhomeinf%2Fsumma7.py;0;4
FILE_NAME_79=0;Python;0;EUTF-8;0;1;1;%2Fhome%2Fedu%2Fhomeinf%2Flycosa-place.py;0;4
FILE_NAME_80=283;Python;0;EUTF-8;0;1;1;%2Fhome%2Fedu%2Fhomeinf%2Fortodroma-commi.py;0;4
FILE_NAME_81=1197;Python;0;EUTF-8;0;1;1;%2Fhome%2Fedu%2Fhomeinf%2Fre-test-dates.py;0;4
FILE_NAME_82=5168;Python;0;EUTF-8;0;1;1;%2Fhome%2Fedu%2Fhomeinf%2Fre-test-words.py;0;4
FILE_NAME_83=100;Python;0;EUTF-8;0;1;1;%2Fhome%2Fedu%2Fhomeinf%2Ftwo-by-three.py;0;4
FILE_NAME_84=0;Python;0;EUTF-8;0;1;1;%2Fhome%2Fedu%2Fhomeinf%2Fwords-order.py;0;4
FILE_NAME_85=1385;Python;0;EUTF-8;0;1;1;%2Fhome%2Fedu%2Fhomeinf%2Fcar-visits.py;0;4
FILE_NAME_86=81;Python;0;EUTF-8;0;1;1;%2Fhome%2Fedu%2Fhomeinf%2Fdet.py;0;4
FILE_NAME_87=588;Python;0;EUTF-8;0;1;1;%2Fhome%2Fpytests%2Ftprofs%2Ftest2.py;0;4
FILE_NAME_88=3209;Python;0;EUTF-8;0;1;1;%2Fhome%2FAIML%2Ftalks%2Fprogs%2Fframes-1%2Fone.py;0;4
FILE_NAME_89=5693;Python;0;EUTF-8;0;1;1;%2Fhome%2FAIML%2Ftalks%2Fprogs%2Fframes-1%2Fpt1.py;0;4
FILE_NAME_90=54;Python;0;EUTF-8;0;1;1;%2Fhome%2Fedu%2Fhomeinf%2Fpermut.py;0;4
FILE_NAME_91=1026;Python;0;EUTF-8;0;1;1;%2Fhome%2Fedu%2Fhomeinf%2Fvasya-amigos.py;0;4
FILE_NAME_92=0;Python;0;EUTF-8;0;1;1;%2Fhome%2Fedu%2Fhomeinf%2Fdiv-sort.py;0;4
FILE_NAME_93=5044;Python;0;EUTF-8;0;1;1;%2Fhome%2Fedu%2Fhomeinf%2Favia-codes.py;0;4
FILE_NAME_94=0;Python;0;EUTF-8;0;1;1;%2Fhome%2Fedu%2Fhomeinf%2Fgamma.py;0;4
FILE_NAME_95=19337;Python;0;EUTF-8;0;1;1;%2Fhome%2Fedu%2Fhomeinf%2Flondon-boros.py;0;4
FILE_NAME_96=9257;Python;0;EUTF-8;0;1;1;%2Fhome%2Fedu%2Fhomeinf%2Fre-test-classic.py;0;4
FILE_NAME_97=1131;Python;0;EUTF-8;0;1;1;%2Fhome%2Fedu%2Fhomeinf%2Fre-test-dates-simple.py;0;4
FILE_NAME_98=77;Python;0;EUTF-8;0;1;1;%2Fhome%2Fedu%2Fhomeinf%2Fre-firms-freq.py;0;4
FILE_NAME_99=1684;Python;0;EUTF-8;0;1;1;%2Fhome%2Fedu%2Fhomeinf%2Fortodroma-def.py;0;4
FILE_NAME_100=670;Python;0;EUTF-8;0;1;1;%2Fhome%2Fedu%2Fhomeinf%2Frot-array-shift.py;0;4
FILE_NAME_101=0;Python;0;EUTF-8;0;1;1;%2Fhome%2Fedu%2Fhomeinf%2Farray-max3-abs.py;0;4
FILE_NAME_102=753;Python;0;EUTF-8;0;1;1;%2Fhome%2Fedu%2Fhomeinf%2Frot-array.py;0;4
FILE_NAME_103=0;Python;0;EUTF-8;0;1;1;%2Fhome%2Fedu%2Fhomeinf%2Farray-max3.py;0;4
FILE_NAME_104=101;Python;0;EUTF-8;0;1;1;%2Fhome%2Fedu%2Fhomeinf%2Fbridge-europe.py;0;4
FILE_NAME_105=734;Python;0;EUTF-8;0;1;1;%2Fhome%2Fedu%2Fhomeinf%2Fdeep-or-high.py;0;4
FILE_NAME_106=11114;Python;0;EUTF-8;0;1;1;%2Fhome%2Fedu%2Fhomeinf%2Fcar-companies.py;0;4
FILE_NAME_107=0;Python;0;EUTF-8;0;1;1;%2Fhome%2Fedu%2Fhomeinf%2Fnz-regions.py;0;4
FILE_NAME_108=0;Python;0;EUTF-8;0;1;1;%2Fhome%2Fedu%2Fhomeinf%2Fbond.py;0;4
FILE_NAME_109=0;Python;0;EUTF-8;0;1;1;%2Fhome%2Fedu%2Fhomeinf%2Fsingers.py;0;4
FILE_NAME_110=81;Python;0;EUTF-8;0;1;1;%2Fhome%2Fedu%2Fhomeinf%2Fflights.py;0;4
FILE_NAME_111=23;Python;0;EUTF-8;0;1;1;%2Fhome%2Fedu%2Fhomeinf%2Feurope-over.py;0;4
FILE_NAME_112=0;Python;0;EUTF-8;0;1;1;%2Fhome%2Fedu%2Fhomeinf%2Fspb-weather.py;0;4
FILE_NAME_113=0;Python;0;EUTF-8;0;1;1;%2Fhome%2Fedu%2Fhomeinf%2Fuk-premier.py;0;4
FILE_NAME_114=9401;Python;0;EUTF-8;0;1;1;%2Fhome%2Fedu%2Fhomeinf%2Fspb-flats.py;0;4
FILE_NAME_115=101;Python;0;EUTF-8;0;1;1;%2Fhome%2Fedu%2Fhomeinf%2Fuk-great-many.py;0;4
FILE_NAME_116=20261;Python;0;EUTF-8;0;1;1;%2Fhome%2Fedu%2Fhomeinf%2Fuk-great.py;0;4
FILE_NAME_117=0;Python;0;EUTF-8;0;1;1;%2Fhome%2Fedu%2Fhomeinf%2Fkab-aap.py;0;4
FILE_NAME_118=7146;Python;0;EUTF-8;0;1;1;%2Fhome%2Fedu%2Fhomeinf%2Fxml-rss-read.py;0;4
FILE_NAME_119=100;Python;0;EUTF-8;0;1;1;%2Fhome%2Fedu%2Fhomeinf%2Ftex-contents.py;0;4
FILE_NAME_120=0;Python;0;EUTF-8;0;1;1;%2Fhome%2Fedu%2Fhomeinf%2Flit-books.py;0;4
FILE_NAME_121=240;Python;0;EUTF-8;0;1;1;%2Fhome%2Fedu%2Fhomeinf%2Fbros-books.py;0;4
FILE_NAME_122=8903;Python;0;EUTF-8;0;1;1;%2Fhome%2Fedu%2Fhomeinf%2Ftolstoj-vim.py;0;4
FILE_NAME_123=97;Python;0;EUTF-8;0;1;1;%2Fhome%2Fedu%2Fhomeinf%2Flit-nobel.py;0;4
FILE_NAME_124=5897;Python;0;EUTF-8;0;1;1;%2Fhome%2Fedu%2Fhomeinf%2Fsmartphones.py;0;4
FILE_NAME_125=5543;Python;0;EUTF-8;0;1;1;%2Fhome%2Fedu%2Fhomeinf%2Flangs-europe.py;0;4
FILE_NAME_126=4601;Python;0;EUTF-8;0;1;1;%2Fhome%2Fedu%2Fhomeinf%2Fnuclear.py;0;4
FILE_NAME_127=595;Python;0;EUTF-8;0;1;1;%2Fhome%2Fedu%2Fhomeinf%2Flangs-eu-borrow.py;0;4
FILE_NAME_128=4922;Python;0;EUTF-8;0;1;1;%2Fhome%2Fedu%2Fhomeinf%2Fkola-passes.py;0;4
FILE_NAME_129=0;Python;0;EUTF-8;0;1;1;%2Fhome%2Fedu%2Fhomeinf%2Fmat-hist.py;0;4
FILE_NAME_130=687;Python;0;EUTF-8;0;1;1;%2Fhome%2Fedu%2Fhomeinf%2Fplanets.py;0;4
FILE_NAME_131=396;Python;0;EUTF-8;0;1;1;%2Fhome%2Fedu%2Fhomeinf%2Fstars.py;0;4
FILE_NAME_132=14230;Python;0;EUTF-8;0;1;1;%2Fhome%2Fedu%2Fhomeinf%2Fpop-coef.py;0;4
FILE_NAME_133=9944;Python;0;EUTF-8;0;1;1;%2Fhome%2Fedu%2Fhomeinf%2Fpaint-rus.py;0;4
FILE_NAME_134=30663;Python;0;EUTF-8;0;1;1;%2Fhome%2Fedu%2Fhomeinf%2Fsoviet-leaders.py;0;4
FILE_NAME_135=14090;Python;0;EUTF-8;0;1;1;%2Fhome%2Fedu%2Fhomeinf%2Fworld-leaders.py;0;4
FILE_NAME_136=6483;Python;0;EUTF-8;0;1;1;%2Fhome%2Fedu%2Fhomeinf%2Fproglangs-pop.py;0;4
FILE_NAME_137=10984;Python;0;EUTF-8;0;1;1;%2Fhome%2Fedu%2Fhomeinf%2Fprogide-hist.py;0;4
FILE_NAME_138=18610;Python;0;EUTF-8;0;1;1;%2Fhome%2Fedu%2Fhomeinf%2Falpha-cities.py;0;4
FILE_NAME_139=6168;Python;0;EUTF-8;0;1;1;%2Fhome%2Fedu%2Fhomeinf%2Fspb-aqi.py;0;4
FILE_NAME_140=26616;Python;0;EUTF-8;0;1;1;%2Fhome%2Fedu%2Fhomeinf%2Ftelemasts.py;0;4
FILE_NAME_141=97;Python;0;EUTF-8;0;1;1;%2Fhome%2Fedu%2Fhomeinf%2Feuro-demo.py;0;4
FILE_NAME_142=99;Python;0;EUTF-8;0;1;1;%2Fhome%2Fedu%2Fhomeinf%2Fstudy-geany.py;0;4

[VTE]
last_dir=/home/edu/homeinf

[build-menu]
EX_00_LB=_Execute
EX_00_CM=python3.14 "%f"
EX_00_WD=
PythonFT_00_LB=_Compile
PythonFT_00_CM=python3.14 -m py_compile "%f"
PythonFT_00_WD=
filetypes=Python;
PythonFT_01_LB=UV run
PythonFT_01_CM=uv run "%f"
PythonFT_01_WD=
"""

# ------------------------------------------------------

parts = files = pythons = 0

for line in data.strip().split('\n'):
    if line.startswith('['):
        parts += 1
    elif line.startswith('FILE_NAME_'):
        files += 1
	# pythons += ";Python" in line
        if ";Python;" in line:
            pythons += 1
    elif line.startswith('EX_00_CM='):
        pv, _ = line.split(' ', maxsplit=1)
        _, ver = pv.split('=')


print(f"""
всего частей:      {parts:5}
всего файлов:      {files:5}
всего питоновских: {pythons:5}
версия питона:       {ver}
""")

# ~ всего частей:          8
# ~ всего файлов:        143
# ~ всего питоновских:   138

# ------------------------------------------------------
