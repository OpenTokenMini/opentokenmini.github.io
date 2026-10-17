"""Writes es/index.html and zh/index.html from index.html (English is the source). Run after editing index.html."""
import pathlib

SRC = pathlib.Path(__file__).parent / "index.html"

COMMON = [
    ('aria-current="page">English</a>', '>English</a>'),
]

LANGS = {
    "es": [
        ('<html lang="en">', '<html lang="es">'),
        ("OpenTokenMini: see what your AI agents spend, and what you get for it",
         "OpenTokenMini: qué gastan tus agentes de IA y qué obtienes a cambio"),
        ("An open method and reference implementation to see what AI agents spend, on what work, and what comes out of it.",
         "Un método abierto y una implementación de referencia para ver cuánto gastan los agentes de IA, en qué trabajo y qué sale de eso."),
        ("Most teams paying for AI agents can't say what the money buys. An open method and reference implementation to find out, across OpenAI, Anthropic and open models.",
         "La mayoría de los equipos que pagan por agentes de IA no sabe qué está comprando con ese dinero. Un método abierto y una implementación de referencia para averiguarlo, con OpenAI, Anthropic y modelos abiertos."),
        ('<link rel="canonical" href="https://opentokenmini.org/">', '<link rel="canonical" href="https://opentokenmini.org/es/">'),
        ('<meta property="og:url" content="https://opentokenmini.org/">', '<meta property="og:url" content="https://opentokenmini.org/es/">'),
        ("Read the method →", "Leer el método →"),
        ("Get the code →", "Ver el código →"),
        ("Most teams paying for AI agents can't say what the money buys.",
         "La mayoría de los equipos que pagan por agentes de IA no sabe qué está comprando con ese dinero."),
        ("OpenTokenMini is an open method and reference implementation to find out: what each agent spends, on which work, and what came out of it. Across OpenAI, Anthropic and open models.",
         "OpenTokenMini es un método abierto y una implementación de referencia para averiguarlo: cuánto gasta cada agente, en qué trabajo y qué salió de ahí. Con OpenAI, Anthropic y modelos abiertos."),
        ("Agent spend by vendor, split by the work it went to and what came out of it",
         "Gasto de agentes por proveedor, dividido por el trabajo al que fue y lo que salió de él"),
        ("Free and open source. Your own agent installs it and fits it to your setup. Unusual setup, or want it built for you?",
         "Libre y de código abierto. Tu propio agente lo instala y lo adapta a tu entorno. ¿Tu entorno es poco común o prefieres que lo armemos nosotros?"),
        ("Talk to us, we build it with you →", "Hablemos, lo armamos contigo →"),
        ('hreflang="es">Español</a>', 'hreflang="es" aria-current="page">Español</a>'),
    ],
    "zh": [
        ('<html lang="en">', '<html lang="zh-Hans">'),
        ("OpenTokenMini: see what your AI agents spend, and what you get for it",
         "OpenTokenMini：看清 AI 智能体花了多少钱，换来了什么"),
        ("An open method and reference implementation to see what AI agents spend, on what work, and what comes out of it.",
         "一套开放的方法和参考实现，用来看清 AI 智能体花了多少钱、花在什么工作上、产出了什么。"),
        ("Most teams paying for AI agents can't say what the money buys. An open method and reference implementation to find out, across OpenAI, Anthropic and open models.",
         "大多数为 AI 智能体付费的团队，说不清这笔钱买到了什么。一套开放的方法和参考实现，帮你弄清楚，支持 OpenAI、Anthropic 和开源模型。"),
        ('<link rel="canonical" href="https://opentokenmini.org/">', '<link rel="canonical" href="https://opentokenmini.org/zh/">'),
        ('<meta property="og:url" content="https://opentokenmini.org/">', '<meta property="og:url" content="https://opentokenmini.org/zh/">'),
        ("Read the method →", "阅读方法 →"),
        ("Get the code →", "获取代码 →"),
        ("Most teams paying for AI agents can't say what the money buys.",
         "大多数为 AI 智能体付费的团队，说不清这笔钱买到了什么。"),
        ("OpenTokenMini is an open method and reference implementation to find out: what each agent spends, on which work, and what came out of it. Across OpenAI, Anthropic and open models.",
         "OpenTokenMini 是一套开放的方法和参考实现，用来回答这个问题：每个智能体花了多少，花在什么工作上，最后产出了什么。支持 OpenAI、Anthropic 和开源模型。"),
        ("Agent spend by vendor, split by the work it went to and what came out of it",
         "按厂商划分的智能体花费，以及它流向的工作和最终产出"),
        ("Free and open source. Your own agent installs it and fits it to your setup. Unusual setup, or want it built for you?",
         "免费开源。由你自己的智能体安装，并按你的环境调整。环境比较特殊，或者希望我们来搭建？"),
        ("Talk to us, we build it with you →", "联系我们，一起搭建 →"),
        ('hreflang="zh-Hans">中文</a>', 'hreflang="zh-Hans" aria-current="page">中文</a>'),
    ],
}

src = SRC.read_text()
for lang, pairs in LANGS.items():
    out = src
    for a, b in COMMON + pairs:
        assert a in out, f"{lang}: missing {a[:60]!r}"
        out = out.replace(a, b)
    (SRC.parent / lang).mkdir(exist_ok=True)
    (SRC.parent / lang / "index.html").write_text(out)
