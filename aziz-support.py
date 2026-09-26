import os
from flask import Flask, render_template_string

app = Flask(__name__)

# أرقام الهواتف والاتصال
KOREK_NUM = "9647519356812"
ASIA_NUM = "9647716001163"

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>عزيز ابن الحجي | مركز حل المشاكل الرقمية والأمان</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link href="https://fonts.googleapis.com/css2?family=Tajawal:wght@400;600;700;800;900&display=swap" rel="stylesheet">
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css" rel="stylesheet">
    <style>
        :root {
            --bg-deep: #05070e;
            --accent-cyan: #00f2fe;
            --korek-color: #0284c7;
            --asia-color: #dc2626;
            --emerald: #10b981;
            --gold: #f59e0b;
            --glass-bg: rgba(13, 19, 33, 0.88);
            --border-glass: rgba(255, 255, 255, 0.08);
            --text-main: #f8fafc;
            --text-sub: #94a3b8;
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Tajawal', sans-serif;
            -webkit-tap-highlight-color: transparent;
        }

        body {
            background-color: var(--bg-deep);
            color: var(--text-main);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 25px 15px;
            position: relative;
        }

        .bg-grid {
            position: fixed;
            top: 0; left: 0; width: 100%; height: 100%;
            background-image: 
                linear-gradient(rgba(0, 242, 254, 0.03) 1px, transparent 1px),
                linear-gradient(90deg, rgba(0, 242, 254, 0.03) 1px, transparent 1px);
            background-size: 35px 35px;
            z-index: -1;
        }

        .hub-card {
            width: 100%;
            max-width: 500px;
            background: var(--glass-bg);
            backdrop-filter: blur(25px);
            -webkit-backdrop-filter: blur(25px);
            border: 1px solid var(--border-glass);
            border-radius: 28px;
            padding: 35px 22px;
            box-shadow: 0 25px 50px rgba(0, 0, 0, 0.7);
            position: relative;
            text-align: center;
        }

        .hub-card::before {
            content: '';
            position: absolute;
            inset: 0;
            border-radius: 28px;
            padding: 1px;
            background: linear-gradient(135deg, rgba(0, 242, 254, 0.4), transparent, rgba(245, 158, 11, 0.3));
            -webkit-mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
            -webkit-mask-composite: xor;
            mask-composite: exclude;
            pointer-events: none;
        }

        .avatar-wrap {
            width: 95px;
            height: 95px;
            margin: 0 auto 14px;
            position: relative;
        }

        .avatar-box {
            width: 100%;
            height: 100%;
            border-radius: 50%;
            background: #0b1120;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 42px;
            color: var(--accent-cyan);
            border: 2px solid rgba(0, 242, 254, 0.4);
            box-shadow: 0 0 25px rgba(0, 242, 254, 0.25);
        }

        .live-dot {
            position: absolute;
            bottom: 4px;
            right: 4px;
            width: 14px;
            height: 14px;
            background: #10b981;
            border: 2px solid #05070e;
            border-radius: 50%;
            box-shadow: 0 0 10px #10b981;
        }

        .name-title {
            font-size: 1.65rem;
            font-weight: 900;
            margin-bottom: 4px;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 8px;
            letter-spacing: -0.5px;
        }

        .verified-badge {
            color: #38bdf8;
            font-size: 1.15rem;
        }

        .crown-icon {
            color: var(--gold);
            font-size: 1.1rem;
        }

        .tagline {
            font-size: 0.9rem;
            color: var(--text-sub);
            line-height: 1.5;
            margin-bottom: 22px;
        }

        .section-label {
            display: flex;
            align-items: center;
            justify-content: space-between;
            font-size: 0.88rem;
            font-weight: 800;
            color: #cbd5e1;
            margin: 20px 0 12px;
            text-align: right;
            padding: 0 4px;
        }

        /* صندوق حل المشاكل */
        .problem-selector-box {
            background: rgba(18, 26, 47, 0.65);
            border: 1px solid rgba(0, 242, 254, 0.15);
            border-radius: 20px;
            padding: 16px;
            margin-bottom: 22px;
            text-align: right;
        }

        .problem-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 10px;
            margin-bottom: 14px;
        }

        .problem-card {
            background: rgba(30, 41, 59, 0.45);
            border: 1px solid rgba(255, 255, 255, 0.06);
            border-radius: 14px;
            padding: 12px 10px;
            text-align: center;
            cursor: pointer;
            transition: all 0.2s ease;
        }

        .problem-card:hover, .problem-card.selected {
            background: rgba(0, 242, 254, 0.12);
            border-color: var(--accent-cyan);
            transform: translateY(-2px);
        }

        .problem-card i {
            font-size: 1.4rem;
            color: var(--accent-cyan);
            margin-bottom: 6px;
            display: block;
        }

        .problem-card.danger i { color: #ef4444; }
        .problem-card.danger:hover, .problem-card.danger.selected {
            border-color: #ef4444;
            background: rgba(239, 68, 68, 0.12);
        }

        .problem-card span {
            font-size: 0.82rem;
            font-weight: 700;
            display: block;
        }

        .quick-input {
            width: 100%;
            padding: 11px 14px;
            background: #1e293b;
            border: 1px solid #334155;
            border-radius: 10px;
            color: #fff;
            font-size: 0.88rem;
            outline: none;
            margin-bottom: 10px;
        }
        .quick-input:focus { border-color: var(--accent-cyan); }

        .btn-solve-now {
            width: 100%;
            background: linear-gradient(135deg, #059669, #10b981);
            color: #fff;
            border: none;
            padding: 13px;
            border-radius: 10px;
            font-weight: 800;
            font-size: 0.98rem;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 8px;
            box-shadow: 0 4px 15px rgba(16, 185, 129, 0.25);
            transition: opacity 0.2s;
        }
        .btn-solve-now:hover { opacity: 0.92; }

        /* خطوط الاتصال السريع */
        .contact-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 10px;
            margin-bottom: 22px;
        }

        .contact-card {
            background: rgba(18, 26, 47, 0.6);
            border: 1px solid rgba(255, 255, 255, 0.05);
            border-radius: 16px;
            padding: 12px 10px;
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 4px;
        }

        .contact-card.korek { border-top: 3px solid var(--korek-color); }
        .contact-card.asia { border-top: 3px solid var(--asia-color); }

        .contact-card .network-name { font-size: 0.88rem; font-weight: 800; }
        .contact-card .phone-num { font-size: 0.78rem; color: #cbd5e1; font-weight: 700; direction: ltr; }

        .action-row { display: flex; gap: 6px; width: 100%; margin-top: 6px; }
        .act-btn {
            flex: 1; padding: 7px 0; border-radius: 8px; font-size: 0.76rem; font-weight: 700;
            text-decoration: none; color: #fff; display: inline-flex; align-items: center; justify-content: center; gap: 4px;
        }
        .act-call { background: #1e293b; border: 1px solid #334155; }
        .act-wa { background: #059669; }

        /* الحسابات الرسمية */
        .links-stack { display: flex; flex-direction: column; gap: 9px; }
        .link-pill {
            display: flex; align-items: center; justify-content: space-between;
            padding: 12px 16px; border-radius: 14px; background: rgba(18, 26, 47, 0.5);
            border: 1px solid rgba(255, 255, 255, 0.05); color: var(--text-main);
            text-decoration: none; font-weight: 700; font-size: 0.92rem; transition: all 0.2s ease;
        }
        .link-pill:hover {
            background: rgba(30, 41, 59, 0.8); border-color: rgba(0, 242, 254, 0.3); transform: translateY(-2px);
        }
        .pill-brand { display: flex; align-items: center; gap: 12px; }
        .pill-brand i { font-size: 1.3rem; width: 22px; text-align: center; }

        .footer-tag { margin-top: 24px; font-size: 0.76rem; color: #64748b; }
    </style>
</head>
<body>

    <div class="bg-grid"></div>

    <div class="hub-card">
        <!-- البروفايل باسم عزيز ابن الحجي -->
        <div class="avatar-wrap">
            <div class="avatar-box"><i class="fa-solid fa-user-shield"></i></div>
            <div class="live-dot" title="متاح 24 ساعة"></div>
        </div>

        <h1 class="name-title">
            <i class="fa-solid fa-crown crown-icon"></i>
            عزيز ابن الحجي
            <i class="fa-solid fa-circle-check verified-badge"></i>
        </h1>
        <p class="tagline">خدمات الدعم الفني والحماية الرقمية | حل مشاكل التعطيل، الابتزاز، واسترجاع الحسابات بسعر مناسب وسرية تامة.</p>

        <!-- قسم حل المشاكل المباشر -->
        <div class="section-label">
            <span><i class="fa-solid fa-bolt" style="color: var(--accent-cyan);"></i> شعندك مشكلة بالإنترنت؟ اختر لنحلها لك:</span>
        </div>

        <div class="problem-selector-box">
            <div class="problem-grid">
                <div class="problem-card selected" onclick="selectProblem(this, 'فك تعطيل / تبنيد حساب')">
                    <i class="fa-solid fa-user-slash"></i>
                    <span>حساب معطل أو متبند</span>
                </div>
                <div class="problem-card danger" onclick="selectProblem(this, 'ابتزاز أو تهديد إلكتروني')">
                    <i class="fa-solid fa-shield-virus"></i>
                    <span>تهديد أو ابتزاز</span>
                </div>
                <div class="problem-card" onclick="selectProblem(this, 'استرجاع حساب مخترق')">
                    <i class="fa-solid fa-key"></i>
                    <span>اختراق وسرقة حساب</span>
                </div>
                <div class="problem-card" onclick="selectProblem(this, 'مشكلة تقنية أخرى')">
                    <i class="fa-solid fa-screwdriver-wrench"></i>
                    <span>مشكلة أخرى</span>
                </div>
            </div>

            <input type="text" id="userTag" class="quick-input" placeholder="اسم المستخدم (@username) أو رابط الحساب">
            
            <div style="display: flex; gap: 8px; margin-bottom: 10px;">
                <select id="lineChoice" class="quick-input" style="margin-bottom:0; width:50%;">
                    <option value="korek">إرسال لخط كورك</option>
                    <option value="asia">إرسال لخط آسيا</option>
                </select>
                <select id="platformChoice" class="quick-input" style="margin-bottom:0; width:50%;">
                    <option value="انستغرام">انستغرام</option>
                    <option value="تيك توك">تيك توك</option>
                    <option value="فيسبوك">فيسبوك</option>
                    <option value="أخرى">منصة أخرى</option>
                </select>
            </div>

            <button type="button" class="btn-solve-now" onclick="sendProblem()">
                <i class="fa-brands fa-whatsapp fa-lg"></i> إرسال المشكلة لعزيز ابن الحجي
            </button>
        </div>

        <!-- أرقام الاتصال المباشر (كورك + آسيا) -->
        <div class="section-label">
            <span><i class="fa-solid fa-phone-volume" style="color: var(--accent-cyan);"></i> اتصال وتواصل مباشر:</span>
        </div>

        <div class="contact-grid">
            <div class="contact-card korek">
                <span class="network-name" style="color: var(--korek-color);">قسم كورك</span>
                <span class="phone-num">+{{ korek_num }}</span>
                <div class="action-row">
                    <a href="tel:+{{ korek_num }}" class="act-btn act-call"><i class="fa-solid fa-phone"></i> اتصال</a>
                    <a href="https://wa.me/{{ korek_num }}" target="_blank" class="act-btn act-wa"><i class="fa-brands fa-whatsapp"></i> واتساب</a>
                </div>
            </div>

            <div class="contact-card asia">
                <span class="network-name" style="color: var(--asia-color);">قسم آسيا</span>
                <span class="phone-num">+{{ asia_num }}</span>
                <div class="action-row">
                    <a href="tel:+{{ asia_num }}" class="act-btn act-call"><i class="fa-solid fa-phone"></i> اتصال</a>
                    <a href="https://wa.me/{{ asia_num }}" target="_blank" class="act-btn act-wa"><i class="fa-brands fa-whatsapp"></i> واتساب</a>
                </div>
            </div>
        </div>

        <!-- الحسابات الرسمية -->
        <div class="section-label">
            <span><i class="fa-solid fa-globe" style="color: var(--accent-cyan);"></i> حساباتي الرسمية:</span>
        </div>

        <div class="links-stack">
            <a href="https://www.instagram.com/aziz_s_hussein?stkn=MXNkMjcyZDk5MTNs" target="_blank" class="link-pill">
                <div class="pill-brand">
                    <i class="fa-brands fa-instagram" style="color: #e1306c;"></i>
                    <span>Instagram | إنستغرام</span>
                </div>
                <i class="fa-solid fa-chevron-left" style="font-size:0.8rem; color:#64748b;"></i>
            </a>

            <a href="https://www.tiktok.com/@2ztsc?_r=1&_t=ZS-9A3in8B25wK" target="_blank" class="link-pill">
                <div class="pill-brand">
                    <i class="fa-brands fa-tiktok" style="color: #00f2fe;"></i>
                    <span>TikTok | تيك توك</span>
                </div>
                <i class="fa-solid fa-chevron-left" style="font-size:0.8rem; color:#64748b;"></i>
            </a>

            <a href="https://youtube.com/@aziz.s.hussein?si=m0-WbZmLohcMc9Ug" target="_blank" class="link-pill">
                <div class="pill-brand">
                    <i class="fa-brands fa-youtube" style="color: #ff0000;"></i>
                    <span>YouTube | يوتيوب</span>
                </div>
                <i class="fa-solid fa-chevron-left" style="font-size:0.8rem; color:#64748b;"></i>
            </a>

            <a href="https://www.facebook.com/share/1Lii7NCbn5/" target="_blank" class="link-pill">
                <div class="pill-brand">
                    <i class="fa-brands fa-facebook" style="color: #1877f2;"></i>
                    <span>Facebook | فيسبوك</span>
                </div>
                <i class="fa-solid fa-chevron-left" style="font-size:0.8rem; color:#64748b;"></i>
            </a>
        </div>

        <div class="footer-tag">
            &copy; عزيز ابن الحجي | الموقع الرسمي الدائم
        </div>
    </div>

<script>
    let currentProblem = 'فك تعطيل / تبنيد حساب';

    function selectProblem(el, problemName) {
        document.querySelectorAll('.problem-card').forEach(c => c.classList.remove('selected'));
        el.classList.add('selected');
        currentProblem = problemName;
    }

    function sendProblem() {
        const userTag = document.getElementById('userTag').value.trim() || 'غير محدد';
        const platform = document.getElementById('platformChoice').value;
        const line = document.getElementById('lineChoice').value;

        const targetPhone = (line === 'korek') ? '{{ korek_num }}' : '{{ asia_num }}';

        const message = `السلام عليكم عزيز ابن الحجي، لدي مشكلة وأحتاج حلاً لها بسعر مناسب:
- نوع المشكلة: ${currentProblem}
- المنصة: ${platform}
- الحساب المعني: ${userTag}`;

        const url = `https://wa.me/${targetPhone}?text=${encodeURIComponent(message)}`;
        window.open(url, '_blank');
    }
</script>

</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(
        HTML_TEMPLATE,
        korek_num=KOREK_NUM,
        asia_num=ASIA_NUM
    )

if __name__ == '__main__':
    # تشغيل إنتاجي دائم ومستقر
    port = int(os.environ.get("PORT", 5000))
    try:
        from waitress import serve
        print(f"الموقع يعمل بشكل دائم ومستقر على المنفذ: {port}")
        serve(app, host='0.0.0.0', port=port)
    except ImportError:
        app.run(host='0.0.0.0', port=port, debug=False)
