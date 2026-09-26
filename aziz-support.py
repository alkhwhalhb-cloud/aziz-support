import os
from flask import Flask, render_template_string

app = Flask(__name__)

# بيانات الاتصال وأرقام الهواتف
KOREK_NUM = "9647519356812"
ASIA_NUM = "9647716001163"

# روابط الحسابات الرسمية
INSTAGRAM_URL = "https://www.instagram.com/aziz_s_hussein?stkn=MXNkMjcyZDk5MTNs"
TIKTOK_URL = "https://www.tiktok.com/@2ztsc?_r=1&_t=ZS-9A3in8B25wK"
FACEBOOK_URL = "https://www.facebook.com/share/1Lii7NCbn5/"
YOUTUBE_URL = "https://youtube.com/@aziz.s.hussein?si=m0-WbZmLohcMc9Ug"

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>عزيز ابن الحجي | بوابة الدعم الفني واسترجاع الحسابات</title>
    <!-- خط تجوال العصري -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Tajawal:wght@400;500;700;800;900&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css">
    <style>
        :root {
            --primary: #0284c7;
            --primary-glow: rgba(2, 132, 199, 0.4);
            --accent: #38bdf8;
            --bg-color: #070d18;
            --card-bg: rgba(15, 23, 42, 0.75);
            --card-border: rgba(56, 189, 248, 0.15);
            --text-main: #f8fafc;
            --text-muted: #94a3b8;
            --success: #10b981;
            --whatsapp: #25d366;
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            font-family: 'Tajawal', sans-serif;
            -webkit-tap-highlight-color: transparent;
        }

        body {
            background-color: var(--bg-color);
            background-image: 
                radial-gradient(at 0% 0%, rgba(2, 132, 199, 0.18) 0px, transparent 50%),
                radial-gradient(at 100% 100%, rgba(56, 189, 248, 0.12) 0px, transparent 50%);
            background-attachment: fixed;
            color: var(--text-main);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 25px 15px;
        }

        .main-card {
            width: 100%;
            max-width: 580px;
            background: var(--card-bg);
            backdrop-filter: blur(16px);
            -webkit-backdrop-filter: blur(16px);
            border: 1px solid var(--card-border);
            border-radius: 28px;
            padding: 35px 25px;
            box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.7);
            position: relative;
            overflow: hidden;
        }

        .main-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 4px;
            background: linear-gradient(90deg, #0284c7, #38bdf8, #10b981);
        }

        /* رأس الصفحة */
        .hero {
            text-align: center;
            margin-bottom: 25px;
        }

        /* العنوان العلوي: عزيز ابن الحجي */
        .brand-top {
            display: inline-block;
            font-size: 26px;
            font-weight: 900;
            color: #ffffff;
            text-shadow: 0 0 15px rgba(56, 189, 248, 0.6);
            letter-spacing: 0.5px;
            margin-bottom: 12px;
            padding: 4px 16px;
            border-radius: 12px;
            background: rgba(255, 255, 255, 0.03);
            border: 1px solid rgba(56, 189, 248, 0.2);
        }

        .hero-badge {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            background: rgba(16, 185, 129, 0.1);
            border: 1px solid rgba(16, 185, 129, 0.3);
            color: var(--success);
            padding: 5px 14px;
            border-radius: 50px;
            font-size: 13px;
            font-weight: 700;
            margin-bottom: 14px;
        }

        .pulse-dot {
            width: 8px;
            height: 8px;
            background: var(--success);
            border-radius: 50%;
            box-shadow: 0 0 10px var(--success);
            animation: pulse 2s infinite;
        }

        @keyframes pulse {
            0%, 100% { opacity: 1; transform: scale(1); }
            50% { opacity: 0.4; transform: scale(1.2); }
        }

        .hero-title {
            font-size: 23px;
            font-weight: 800;
            line-height: 1.35;
            margin-bottom: 8px;
        }

        .hero-title span {
            background: linear-gradient(135deg, #38bdf8, #0284c7);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        .hero-sub {
            color: var(--text-muted);
            font-size: 14px;
            line-height: 1.6;
        }

        /* مميزات الخدمة */
        .features-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 10px;
            margin-bottom: 25px;
        }

        .feature-box {
            background: rgba(255, 255, 255, 0.03);
            border: 1px solid rgba(255, 255, 255, 0.06);
            border-radius: 14px;
            padding: 12px 8px;
            text-align: center;
            transition: all 0.3s ease;
        }

        .feature-box i {
            font-size: 20px;
            color: var(--accent);
            margin-bottom: 6px;
        }

        .feature-box p {
            font-size: 12px;
            font-weight: 700;
            color: #e2e8f0;
        }

        /* النموذج */
        .form-section {
            display: flex;
            flex-direction: column;
            gap: 15px;
        }

        .input-group {
            display: flex;
            flex-direction: column;
            gap: 6px;
        }

        .input-group label {
            font-size: 13.5px;
            font-weight: 700;
            color: #cbd5e1;
            display: flex;
            align-items: center;
            gap: 6px;
        }

        .input-group label i {
            color: var(--accent);
            font-size: 14px;
        }

        .custom-input {
            width: 100%;
            background: rgba(10, 16, 30, 0.85);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 12px;
            padding: 12px 14px;
            color: #fff;
            font-size: 14px;
            outline: none;
            transition: all 0.25s ease;
        }

        .custom-input:focus {
            border-color: var(--accent);
            box-shadow: 0 0 12px var(--primary-glow);
            background: rgba(10, 16, 30, 1);
        }

        .btn-whatsapp {
            width: 100%;
            padding: 14px;
            margin-top: 5px;
            background: linear-gradient(135deg, #25d366, #128c7e);
            color: #fff;
            border: none;
            border-radius: 14px;
            font-size: 16px;
            font-weight: 800;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 10px;
            box-shadow: 0 10px 20px -5px rgba(37, 211, 102, 0.35);
            transition: all 0.25s ease;
        }

        .btn-whatsapp:active {
            transform: scale(0.98);
        }

        /* أزرار الاتصال */
        .divider {
            display: flex;
            align-items: center;
            text-align: center;
            margin: 25px 0 15px;
            color: var(--text-muted);
            font-size: 12px;
            font-weight: 600;
        }

        .divider::before, .divider::after {
            content: '';
            flex: 1;
            border-bottom: 1px solid rgba(255, 255, 255, 0.08);
        }

        .divider:not(:empty)::before { margin-left: .8em; }
        .divider:not(:empty)::after { margin-right: .8em; }

        .call-buttons {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 10px;
        }

        .call-btn {
            padding: 11px;
            border-radius: 12px;
            text-decoration: none;
            color: #fff;
            font-size: 13px;
            font-weight: 700;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 8px;
            border: 1px solid rgba(255, 255, 255, 0.1);
        }

        .call-btn.korek { background: linear-gradient(135deg, #047857, #065f46); }
        .call-btn.asia { background: linear-gradient(135deg, #be123c, #9f1239); }

        /* حسابات التواصل */
        .social-row {
            display: flex;
            justify-content: center;
            gap: 12px;
            margin-top: 15px;
        }

        .social-pill {
            width: 44px;
            height: 44px;
            border-radius: 12px;
            background: rgba(255, 255, 255, 0.04);
            border: 1px solid rgba(255, 255, 255, 0.08);
            display: flex;
            align-items: center;
            justify-content: center;
            color: #fff;
            font-size: 18px;
            text-decoration: none;
            transition: all 0.25s ease;
        }

        .social-pill:hover {
            transform: translateY(-3px);
            background: rgba(255, 255, 255, 0.12);
        }

        .social-pill.insta:hover { color: #e1306c; border-color: #e1306c; }
        .social-pill.tiktok:hover { color: #00f2fe; border-color: #00f2fe; }
        .social-pill.fb:hover { color: #1877f2; border-color: #1877f2; }
        .social-pill.yt:hover { color: #ff0000; border-color: #ff0000; }

        .footer-note {
            text-align: center;
            margin-top: 20px;
            font-size: 11.5px;
            color: var(--text-muted);
        }
    </style>
</head>
<body>

<div class="main-card">
    <div class="hero">
        <!-- الاسم الفخم في الأعلى -->
        <div class="brand-top">👑 عزيز ابن الحجي</div>
        <br>
        <div class="hero-badge">
            <span class="pulse-dot"></span> استجابة فنية مباشرة
        </div>
        <h1 class="hero-title">مركز حل المشاكل و<span>استرجاع الحسابات</span></h1>
        <p class="hero-sub">خدمة موثوقة لمساعدتك في استعادة وتأمين حساباتك المعطلة أو المفقودة بطرق نظامية وآمنة.</p>
    </div>

    <div class="features-grid">
        <div class="feature-box">
            <i class="fa-solid fa-lock-open"></i>
            <p>استرجاع الحسابات</p>
        </div>
        <div class="feature-box">
            <i class="fa-solid fa-key"></i>
            <p>حل مشاكل 2FA</p>
        </div>
        <div class="feature-box">
            <i class="fa-solid fa-shield-virus"></i>
            <p>تأمين الحماية</p>
        </div>
    </div>

    <form class="form-section" onsubmit="sendWhatsApp(event)">
        <div class="input-group">
            <label><i class="fa-solid fa-layer-group"></i> نوع المنصة / التطبيق</label>
            <select id="platform" class="custom-input" required>
                <option value="Instagram">إنستغرام (Instagram)</option>
                <option value="Facebook">فيسبوك (Facebook)</option>
                <option value="TikTok">تيك توك (TikTok)</option>
                <option value="Snapchat">سناب شات (Snapchat)</option>
                <option value="Telegram">تيليجرام (Telegram)</option>
                <option value="Gmail">جوجل / جيميل (Gmail)</option>
            </select>
        </div>

        <div class="input-group">
            <label><i class="fa-solid fa-circle-exclamation"></i> طبيعة المشكلة</label>
            <select id="issue" class="custom-input" required>
                <option value="الحساب مخترق وتم تغيير معلوماته">الحساب مخترق وتم تغيير معلوماته</option>
                <option value="الحساب مقفل أو معطل احترازياً">الحساب مقفل أو معطل احترازياً</option>
                <option value="مشكلة في رمز التحقق الثنائي (2FA)">مشكلة في رمز التحقق الثنائي (2FA)</option>
                <option value="فقدان البريد أو رقم الهاتف المسجل">فقدان البريد أو رقم الهاتف المسجل</option>
            </select>
        </div>

        <div class="input-group">
            <label><i class="fa-solid fa-at"></i> اسم المستخدم أو الرابط</label>
            <input type="text" id="username" class="custom-input" placeholder="مثال: @username أو الرابط" required>
        </div>

        <div class="input-group">
            <label><i class="fa-solid fa-file-lines"></i> تفاصيل أو ملاحظات إضافية</label>
            <textarea id="details" class="custom-input" rows="2" placeholder="اكتب باختصار متى ظهرت المشكلة وأي بيانات قد تساعد..."></textarea>
        </div>

        <button type="submit" class="btn-whatsapp">
            <i class="fa-brands fa-whatsapp"></i> إرسال الطلب للمراجعة والحل
        </button>
    </form>

    <div class="divider">الاتصال المباشر والدعم</div>

    <div class="call-buttons">
        <a href="tel:{{ korek }}" class="call-btn korek">
            <i class="fa-solid fa-phone"></i> كورك: {{ korek }}
        </a>
        <a href="tel:{{ asia }}" class="call-btn asia">
            <i class="fa-solid fa-phone"></i> آسيا: {{ asia }}
        </a>
    </div>

    <div class="divider">الحسابات والمنصات الرسمية</div>

    <div class="social-row">
        <a href="{{ insta }}" target="_blank" class="social-pill insta" title="Instagram">
            <i class="fa-brands fa-instagram"></i>
        </a>
        <a href="{{ tiktok }}" target="_blank" class="social-pill tiktok" title="TikTok">
            <i class="fa-brands fa-tiktok"></i>
        </a>
        <a href="{{ fb }}" target="_blank" class="social-pill fb" title="Facebook">
            <i class="fa-brands fa-facebook-f"></i>
        </a>
        <a href="{{ yt }}" target="_blank" class="social-pill yt" title="YouTube">
            <i class="fa-brands fa-youtube"></i>
        </a>
    </div>

    <p class="footer-note">جميع العمليات تخضع للسياسات الأمنية والمعايير الفنية المعتمدة للمنصات.</p>
</div>

<script>
function sendWhatsApp(e) {
    e.preventDefault();
    const platform = document.getElementById('platform').value;
    const issue = document.getElementById('issue').value;
    const username = document.getElementById('username').value;
    const details = document.getElementById('details').value;

    const message = `مرحباً، أود تقديم طلب استرجاع / حل مشكلة تقنية:%0A%0A` +
                    `👑 *المسؤول:* عزيز ابن الحجي%0A` +
                    `🔹 *المنصة:* ${platform}%0A` +
                    `⚠️ *نوع المشكلة:* ${issue}%0A` +
                    `👤 *الحساب:* ${username}%0A` +
                    `📝 *ملاحظات:* ${details ? details : 'لا توجد'}`;

    const phone = "{{ korek }}";
    window.open(`https://wa.me/${phone}?text=${message}`, '_blank');
}
</script>

</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(
        HTML_TEMPLATE,
        korek=KOREK_NUM,
        asia=ASIA_NUM,
        insta=INSTAGRAM_URL,
        tiktok=TIKTOK_URL,
        fb=FACEBOOK_URL,
        yt=YOUTUBE_URL
    )

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
