#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2026
# tex-contents.py
# 2026-06-23 2026-06-23 1.1
# Составление содержания статьи в ТеХе
# Ищем section, subsection

import re

# ---------------------- data -------------------------------

article = r"""
% Options for packages loaded elsewhere
\PassOptionsToPackage{unicode}{hyperref}
\PassOptionsToPackage{hyphens}{url}
%
\documentclass[]{article}
\usepackage{lmodern}
\usepackage{amssymb,amsmath}
\usepackage{ifxetex,ifluatex}
\ifnum 0\ifxetex 1\fi\ifluatex 1\fi=0 % if pdftex
  \usepackage[T1]{fontenc}
  \usepackage[utf8]{inputenc}
  \usepackage{textcomp} % provide euro and other symbols
\else % if luatex or xetex
  \usepackage{unicode-math}
  \defaultfontfeatures{Scale=MatchLowercase}
  \defaultfontfeatures[\rmfamily]{Ligatures=TeX,Scale=1}
\fi
% Use upquote if available, for straight quotes in verbatim environments
\IfFileExists{upquote.sty}{\usepackage{upquote}}{}
\IfFileExists{microtype.sty}{% use microtype if available
  \usepackage[]{microtype}
  \UseMicrotypeSet[protrusion]{basicmath} % disable protrusion for tt fonts
}{}
\makeatletter
\@ifundefined{KOMAClassName}{% if non-KOMA class
  \IfFileExists{parskip.sty}{%
    \usepackage{parskip}
  }{% else
    \setlength{\parindent}{0pt}
    \setlength{\parskip}{6pt plus 2pt minus 1pt}}
}{% if KOMA class
  \KOMAoptions{parskip=half}}
\makeatother
\usepackage{xcolor}
\IfFileExists{xurl.sty}{\usepackage{xurl}}{} % add URL line breaks if available
\IfFileExists{bookmark.sty}{\usepackage{bookmark}}{\usepackage{hyperref}}
\hypersetup{
  pdftitle={Noosphere simulation, or Project 4x4},
  pdfauthor={Mikhail Kolodin},
  hidelinks,
  pdfcreator={LaTeX via pandoc}}
\urlstyle{same} % disable monospaced font for URLs
\setlength{\emergencystretch}{3em} % prevent overfull lines
\providecommand{\tightlist}{%
  \setlength{\itemsep}{0pt}\setlength{\parskip}{0pt}}
\setcounter{secnumdepth}{-\maxdimen} % remove section numbering

\title{Noosphere simulation, or Project 4x4}
\author{Mikhail Kolodin}
\date{2023-03-01}

\begin{document}
\maketitle
\begin{abstract}
The paper deals with general approach to computer simulation of the
Noosphere, using stuctural approach, formulated as 4 stages with several
substages in each.

Results are presented and discussed.
\end{abstract}

\hypertarget{introduction}{%
\section{Introduction}\label{introduction}}

\hypertarget{problem-definition}{%
\subsection{Problem definition}\label{problem-definition}}

In order to control the world, we must understand it.

In order to understand the world, we try to simulate it.

\hypertarget{stages-of-problem-solution}{%
\subsection{Stages of Problem Solution}\label{stages-of-problem-solution}}

The next 4 stages are suggested as frameworks or the research: 1.
getting data, 2. data processing, 3. demonstration of results, 4.
experimenting with results.

Each of them have several sub-stages.

\hypertarget{stage-1.-getting-data}{%
\section{Stage 1. Getting Data}\label{stage-1.-getting-data}}

There are different sources of data we can process.

They are - global: in the internet sites and special pages, databases,
both well structured and irregularily collected, with API or with
necessity of page parsing, - local: in office or office-like files (like
MSO Excel, csv/tsv files, etc).

We must - obtain pages, databases, files (localy or by obtaining remote
access) - get useful information from them (by using API, parsing, etc),
- clean, refill and restructure it for the future use, - organize
regular updates of the information.

So the stages are: 1. getting info, 2. cleaning it, 3. storing in out
text-based structured files or databases, 4. organize updates, on
scedule, with rewriting or updating our databases.

\hypertarget{stage-2.-data-processing}{%
\section{Stage 2. Data Processing}\label{stage-2.-data-processing}}

We can outline 4 principal approaches to simulation: 1. rule-based
step-by-step inference, 2. higher-level modeling: objects-based, 3.
lower-level modeling: e.g.~multi-agent systems, 4. AI/ML approach
(Artificial Intelligence/ Machine Learning).

\hypertarget{stage-3.-demonstration-and-experimenting-with-results}{%
\section{Stage 3. Demonstration and Experimenting with Results}\label{stage-3.-demonstration-and-experimenting-with-results}}

We must 1. show results visually to the researcher as they are, 2. make
simulation ``what if'' (forward spreading), 3. make simulation ``how
to'' (backward spreading), 4. save results instructured texts,
speadsheets and databases and use them for the next processing
(looping).

\hypertarget{stage-4.-domains-implementation-of-results}{%
\section{Stage 4. Domains Implementation of Results}\label{stage-4.-domains-implementation-of-results}}

We apply our research to the following domains: 1. technical sysetms and
processes, 2. biological and ecological systems, 3. social, economic,
political and scientific sphere, 4. all of them together, with their
interrelelations.

\hypertarget{resume}{%
\section{Resume}\label{resume}}

This research is being done for a long time and will continue with its
results being regularily published.

\end{document}
"""

# ---------------------- process -------------------------------

for line, text in enumerate(article.splitlines(), start=1):
    res = re.search(r'\\(?:sub)?section{([^}]+)}', text)
    if res:
        print(f"{line:3}. {'    ' if '\\sub' in text else ''}{res.group(1)}")


# ---------------------- result -------------------------------

 # ~ 65. Introduction
 # ~ 68.     Problem definition
 # ~ 75.     Stages of Problem Solution
 # ~ 84. Stage 1. Getting Data
# ~ 103. Stage 2. Data Processing
# ~ 111. Stage 3. Demonstration and Experimenting with Results
# ~ 120. Stage 4. Domains Implementation of Results
# ~ 128. Resume

# ---------------------- end -------------------------------
