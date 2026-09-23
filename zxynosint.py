# ═══════════════════════════════════════════════════
#  AUTO PACKAGE INSTALLER
# ═══════════════════════════════════════════════════
import subprocess
import sys
import importlib

REQUIRED_PACKAGES = {
    "telebot":        "pyTelegramBotAPI",
    "requests":       "requests",
    "psycopg2":       "psycopg2-binary",
}

def _install_missing():
    missing = []
    for module, pkg in REQUIRED_PACKAGES.items():
        try:
            importlib.import_module(module)
        except ImportError:
            missing.append(pkg)

    if not missing:
        return

    print(f"📦 Installing missing packages: {', '.join(missing)}")
    for pkg in missing:
        try:
            subprocess.check_call(
                [sys.executable, "-m", "pip", "install", "--quiet", "--upgrade", pkg]
            )
            print(f"✅ Installed {pkg}")
        except subprocess.CalledProcessError as e:
            print(f"❌ Failed to install {pkg}: {e}")
            sys.exit(1)

    # Refresh import caches so newly installed modules are visible
    importlib.invalidate_caches()

_install_missing()

# ═══════════════════════════════════════════════════
#  IMPORTS (safe after installer)
# ═══════════════════════════════════════════════════
import telebot
import requests
import psycopg2
from psycopg2 import pool

# ═══════════════════════════════════════════════════
#  CONFIG
# ═══════════════════════════════════════════════════
BOT_TOKEN        = "8108175391:AAGPQMQjcKWIM6EqS90MhQHD0sYsuOoUbN0"
CHANNEL_USERNAME = "@codezxyns"

# ─── DOUBLE ADMIN SYSTEM ───
ADMIN_IDS = [
    8848159805,   # 👑 ᴀᴅᴍɪɴ 1
    8231927184,   # 👑 ᴀᴅᴍɪɴ 2  ← ʀᴇᴘʟᴀᴄᴇ ᴡɪᴛʜ ᴀᴄᴛᴜᴀʟ ɪᴅ
]

# ─── SUPABASE ───
SUPABASE_DB_URL = "postgresql://postgres:ishaaq78600@db.canaorxzjqswolqqexvx.supabase.co:5432/postgres"

# ─── APIs ───
API_NUM     = "https://vtrosint.dpdns.org/?key=vtr_draxion&mobile={num}"
API_AADHAAR = "https://vtrosint.dpdns.org/api/search/aadhaar?id={aadhar_id}&key=vtr_draxion"

OWNER_TEXT = "👑 <b>ᴏᴡɴᴇʀ :</b> @GotHate"

bot = telebot.TeleBot(BOT_TOKEN)

# ═══════════════════════════════════════════════════
#  BUTTON CONSTANTS
# ═══════════════════════════════════════════════════
BTN_SEARCH     = "🔍 ꜱᴇᴀʀᴄʜ"
BTN_BALANCE    = "💰 ʙᴀʟᴀɴᴄᴇ"
BTN_REDEEM     = "🎁 ʀᴇᴅᴇᴇᴍ"
BTN_OWNER      = "👤 ᴏᴡɴᴇʀ"
BTN_ADMIN      = "🛠 ᴀᴅᴍɪɴ ᴘᴀɴᴇʟ"

BTN_S_NUM      = "📱 ɴᴜᴍ ɪɴꜰᴏ"
BTN_S_AADHAAR  = "🆔 ᴀᴀᴅʜᴀᴀʀ ɪɴꜰᴏ"
BTN_BACK       = "⬅️ ʙᴀᴄᴋ"

BTN_BROADCAST  = "📣 ʙʀᴏᴀᴅᴄᴀꜱᴛ"
BTN_CHANNELS   = "📢 ᴄʜᴀɴɴᴇʟꜱ"
BTN_ADD_BAL    = "💰 ᴀᴅᴅ ʙᴀʟᴀɴᴄᴇ"
BTN_REM_BAL    = "➖ ʀᴇᴍᴏᴠᴇ ʙᴀʟᴀɴᴄᴇ"
BTN_BAN        = "🚫 ʙᴀɴ ᴜꜱᴇʀ"
BTN_UNBAN      = "✅ ᴜɴʙᴀɴ ᴜꜱᴇʀ"

# ═══════════════════════════════════════════════════
#  AADHAAR FIELD LABELS
# ═══════════════════════════════════════════════════
AADHAAR_LABELS = {
    'aadhaar':         '🆔 ᴀᴀᴅʜᴀᴀʀ ɴᴏ',
    'aadhar':          '🆔 ᴀᴀᴅʜᴀᴀʀ ɴᴏ',
    'aadhaar_number':  '🆔 ᴀᴀᴅʜᴀᴀʀ ɴᴏ',
    'aadhar_number':   '🆔 ᴀᴀᴅʜᴀᴀʀ ɴᴏ',
    'uid':             '🆔 ᴀᴀᴅʜᴀᴀʀ ɴᴏ',
    'name':            '🫵 ɴᴀᴍᴇ',
    'father_name':     '👨‍👦 ꜰᴀᴛʜᴇʀ',
    'mother_name':     '👩 ᴍᴏᴛʜᴇʀ',
    'dob':             '🎂 ᴅᴏʙ',
    'date_of_birth':   '🎂 ᴅᴏʙ',
    'gender':          '⚧ ɢᴇɴᴅᴇʀ',
    'address':         '🏠 ᴀᴅᴅʀᴇꜱꜱ',
    'mobile':          '📱 ᴍᴏʙɪʟᴇ',
    'mobile_number':   '📱 ᴍᴏʙɪʟᴇ',
    'phone':           '📱 ᴍᴏʙɪʟᴇ',
    'alt_mobile':      '📞 ᴀʟᴛ ᴍᴏʙɪʟᴇ',
    'circle':          '🌐 ᴄɪʀᴄʟᴇ',
    'state':           '🗺 ꜱᴛᴀᴛᴇ',
    'district':        '🏙 ᴅɪꜱᴛʀɪᴄᴛ',
    'pincode':         '📮 ᴘɪɴᴄᴏᴅᴇ',
    'pin_code':        '📮 ᴘɪɴᴄᴏᴅᴇ',
    'email':           '📧 ᴇᴍᴀɪʟ',
    'care_of':         '👥 ᴄᴀʀᴇ ᴏꜰ',
    'record_type':     '📋 ʀᴇᴄᴏʀᴅ ᴛʏᴘᴇ',
}

AADHAAR_SKIP = {
    '_id', 'id', '__v',
    'created_at', 'updated_at',
    'developer', 'team', 'contact', 'owner',
    'plan', 'timestamp', 'endpoint', 'response_time',
}

# ═══════════════════════════════════════════════════
#  DATABASE — SUPABASE (PostgreSQL)
# ═══════════════════════════════════════════════════
try:
    DB_POOL = pool.ThreadedConnectionPool(
        minconn=1,
        maxconn=10,
        dsn=SUPABASE_DB_URL
    )
    print("✅ Supabase pool connected.")
except Exception as e:
    print(f"❌ Supabase connection failed: {e}")
    raise SystemExit

def db_exec(sql, params=(), fetch=None, commit=False):
    conn = None
    try:
        conn = DB_POOL.getconn()
        cur = conn.cursor()
        cur.execute(sql, params)
        result = None
        if fetch == 'one':
            result = cur.fetchone()
        elif fetch == 'all':
            result = cur.fetchall()
        else:
            result = cur.rowcount
        if commit:
            conn.commit()
        cur.close()
        return result
    except Exception:
        if conn:
            try:
                conn.rollback()
            except Exception:
                pass
        raise
    finally:
        if conn:
            DB_POOL.putconn(conn)

# ═══════════════════════════════════════════════════
#  HELPERS
# ═══════════════════════════════════════════════════
def is_owner(user_id):
    return user_id in ADMIN_IDS

def user_exists_prior(user_id):
    row = db_exec("SELECT 1 FROM users WHERE user_id = %s", (user_id,), fetch='one')
    return row is not None

def get_user(user_id):
    db_exec(
        """INSERT INTO users (user_id, balance, verified)
           VALUES (%s, 5, 0)
           ON CONFLICT (user_id) DO NOTHING""",
        (user_id,), commit=True)

    row = db_exec(
        "SELECT user_id, balance, verified FROM users WHERE user_id = %s",
        (user_id,), fetch='one')

    if row is None:
        return {'user_id': user_id, 'balance': 0, 'verified': 0}
    return {'user_id': row[0], 'balance': row[1], 'verified': row[2]}

def update_balance(user_id, amount):
    db_exec("UPDATE users SET balance = balance + %s WHERE user_id = %s",
            (amount, user_id), commit=True)

def set_balance(user_id, amount):
    db_exec(
        """INSERT INTO users (user_id, balance, verified)
           VALUES (%s, %s, 0)
           ON CONFLICT (user_id) DO UPDATE SET balance = EXCLUDED.balance""",
        (user_id, amount), commit=True)

def set_verified(user_id):
    db_exec("UPDATE users SET verified = 1 WHERE user_id = %s",
            (user_id,), commit=True)

def is_banned(user_id):
    if is_owner(user_id):
        return False
    row = db_exec("SELECT 1 FROM banned_users WHERE user_id = %s",
                  (user_id,), fetch='one')
    return bool(row)

def ban_user(user_id, reason="—"):
    db_exec(
        """INSERT INTO banned_users (user_id, reason, banned_at)
           VALUES (%s, %s, NOW())
           ON CONFLICT (user_id) DO UPDATE
           SET reason = EXCLUDED.reason, banned_at = NOW()""",
        (user_id, reason), commit=True)

def unban_user(user_id):
    db_exec("DELETE FROM banned_users WHERE user_id = %s",
            (user_id,), commit=True)

def clean_html(text):
    if text is None or text == "":
        return "ɴ/ᴀ"
    return str(text).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

def get_main_channel():
    row = db_exec("SELECT setting_value FROM bot_settings WHERE setting_key = %s",
                  ("channel_username",), fetch='one')
    return row[0] if row else CHANNEL_USERNAME

def set_main_channel(username):
    global CHANNEL_USERNAME
    CHANNEL_USERNAME = username
    db_exec(
        """INSERT INTO bot_settings (setting_key, setting_value) VALUES (%s, %s)
           ON CONFLICT (setting_key) DO UPDATE SET setting_value = EXCLUDED.setting_value""",
        ("channel_username", username), commit=True)

CHANNEL_USERNAME = get_main_channel()

def balance_text(user_id):
    if is_owner(user_id):
        return "∞ ᴜɴʟɪᴍɪᴛᴇᴅ"
    return str(get_user(user_id)['balance'])

def banned_guard(user_id):
    if is_banned(user_id):
        try:
            bot.send_message(user_id,
                "🚫 <b>ʏᴏᴜ ᴀʀᴇ ʙᴀɴɴᴇᴅ ꜰʀᴏᴍ ᴜꜱɪɴɢ ᴛʜɪꜱ ʙᴏᴛ.</b>",
                parse_mode="HTML")
        except Exception:
            pass
        return True
    return False

def extract_first_data(res):
    if not isinstance(res, dict):
        return None
    if res.get("status") != "success":
        return None
    data = res.get("data")
    if isinstance(data, list):
        return data[0] if data else None
    if isinstance(data, dict):
        return data
    return None

def format_aadhaar(d):
    if not isinstance(d, dict):
        return "❌ <b>ɴᴏ ᴅᴀᴛᴀ ꜰᴏᴜɴᴅ.</b>"

    lines = []
    used = set()

    for key, label in AADHAAR_LABELS.items():
        if key in d and d[key] not in (None, "", "N/A", "n/a"):
            lines.append(f"{label} : <code>{clean_html(d[key])}</code>")
            used.add(key)

    for key, val in d.items():
        if key in used or key in AADHAAR_SKIP:
            continue
        if val in (None, "", "N/A", "n/a"):
            continue
        if isinstance(val, (dict, list)):
            continue
        nice = key.replace("_", " ").upper()
        lines.append(f"• <b>{clean_html(nice)}</b> : <code>{clean_html(val)}</code>")

    if not lines:
        return "❌ <b>ɴᴏ ᴅᴀᴛᴀ ꜰᴏᴜɴᴅ.</b>"

    return (
        "✅ <b>ᴀᴀᴅʜᴀᴀʀ ᴅᴇᴛᴀɪʟꜱ ꜰᴏᴜɴᴅ</b>\n"
        "━━━━━━━━━━━━━━━━━━\n"
        + "\n".join(lines)
    )

# ═══════════════════════════════════════════════════
#  KEYBOARDS
# ═══════════════════════════════════════════════════
def main_menu_keyboard(user_id=None):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    markup.add(telebot.types.KeyboardButton(BTN_SEARCH),
               telebot.types.KeyboardButton(BTN_BALANCE))
    markup.add(telebot.types.KeyboardButton(BTN_REDEEM),
               telebot.types.KeyboardButton(BTN_OWNER))
    if user_id in ADMIN_IDS:
        markup.add(telebot.types.KeyboardButton(BTN_ADMIN))
    return markup

def search_menu_keyboard(user_id=None):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    markup.add(telebot.types.KeyboardButton(BTN_S_NUM),
               telebot.types.KeyboardButton(BTN_S_AADHAAR))
    markup.add(telebot.types.KeyboardButton(BTN_BACK))
    return markup

def admin_panel_keyboard():
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    markup.add(telebot.types.KeyboardButton(BTN_BROADCAST),
               telebot.types.KeyboardButton(BTN_CHANNELS))
    markup.add(telebot.types.KeyboardButton(BTN_ADD_BAL),
               telebot.types.KeyboardButton(BTN_REM_BAL))
    markup.add(telebot.types.KeyboardButton(BTN_BAN),
               telebot.types.KeyboardButton(BTN_UNBAN))
    markup.add(telebot.types.KeyboardButton(BTN_BACK))
    return markup

def force_join_keyboard():
    markup = telebot.types.InlineKeyboardMarkup(row_width=1)
    channel = get_main_channel()
    if channel:
        markup.add(telebot.types.InlineKeyboardButton(
            "📢  ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ",
            url=f"https://t.me/{channel[1:]}"))
        markup.add(telebot.types.InlineKeyboardButton(
            "✅  ɪ ʜᴀᴠᴇ ᴊᴏɪɴᴇᴅ",
            callback_data="verify_join"))
    return markup

def channels_manage_keyboard():
    kb = telebot.types.InlineKeyboardMarkup()
    kb.add(telebot.types.InlineKeyboardButton("➕ ᴀᴅᴅ / ᴄʜᴀɴɢᴇ ᴄʜᴀɴɴᴇʟ",
                                              callback_data="admin_add_channel"))
    kb.add(telebot.types.InlineKeyboardButton("🗑 ʀᴇᴍᴏᴠᴇ ᴄʜᴀɴɴᴇʟ",
                                              callback_data="admin_remove_channel"))
    kb.add(telebot.types.InlineKeyboardButton("⬅️ ʙᴀᴄᴋ",
                                              callback_data="admin_panel_back"))
    return kb

# ═══════════════════════════════════════════════════
#  COMMANDS
# ═══════════════════════════════════════════════════
@bot.message_handler(commands=['start'])
def cmd_start(message):
    uid = message.from_user.id
    if banned_guard(uid):
        return

    was_new = not user_exists_prior(uid)
    user = get_user(uid)
    channel = get_main_channel()

    if was_new:
        for admin in ADMIN_IDS:
            try:
                bot.send_message(admin,
                    f"🆕 <b>ɴᴇᴡ ᴜꜱᴇʀ</b>\n🆔 <code>{uid}</code>",
                    parse_mode="HTML")
            except Exception:
                pass

    if not is_owner(uid) and channel and user['verified'] == 0:
        bot.send_message(
            message.chat.id,
            "🔐 <b>ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ɪꜱʜᴀᴀǫ ɴᴜᴍ ɪɴꜰᴏ ʙᴏᴛ</b>\n"
            "━━━━━━━━━━━━━━━━━━\n\n"
            "📢 ᴊᴏɪɴ ᴛʜᴇ ᴄʜᴀɴɴᴇʟ ʙᴇʟᴏᴡ, ᴛʜᴇɴ ᴛᴀᴘ <b>ɪ ʜᴀᴠᴇ ᴊᴏɪɴᴇᴅ</b>.\n"
            "✅ ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴ ɪꜱ ᴏɴᴇ-ᴛɪᴍᴇ.",
            reply_markup=force_join_keyboard(),
            parse_mode="HTML"
        )
        return

    bot.send_message(
        message.chat.id,
        "👋 <b>ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ɪꜱʜᴀᴀǫ ɴᴜᴍ ɪɴꜰᴏ ʙᴏᴛ</b>\n"
        "━━━━━━━━━━━━━━━━━━\n\n"
        "✨ ᴄʜᴏᴏꜱᴇ ᴀɴ ᴏᴘᴛɪᴏɴ ꜰʀᴏᴍ ᴛʜᴇ ᴍᴇɴᴜ ʙᴇʟᴏᴡ.",
        reply_markup=main_menu_keyboard(uid),
        parse_mode="HTML"
    )

@bot.message_handler(commands=['panel'])
def cmd_panel(message):
    if message.from_user.id not in ADMIN_IDS:
        bot.reply_to(message, "❌ ᴀᴅᴍɪɴ ᴏɴʟʏ.")
        return
    bot.send_message(
        message.chat.id,
        "🛠 <b>ᴀᴅᴍɪɴ ᴘᴀɴᴇʟ</b>\n"
        "━━━━━━━━━━━━━━━━━━\n\n"
        "ᴘɪᴄᴋ ᴀɴ ᴀᴄᴛɪᴏɴ ʙᴇʟᴏᴡ.",
        parse_mode="HTML",
        reply_markup=admin_panel_keyboard()
    )

@bot.message_handler(commands=['redeem'])
def cmd_generate_redeem(message):
    if message.from_user.id not in ADMIN_IDS:
        return
    try:
        parts = message.text.split()
        if len(parts) != 4:
            raise ValueError
        code    = parts[1].upper()
        credits = int(parts[2])
        limit   = int(parts[3])
        if credits <= 0 or limit <= 0 or " " in code:
            raise ValueError
        db_exec(
            """INSERT INTO redeem_codes (code, credits, limit_total, used_count)
               VALUES (%s, %s, %s, 0)
               ON CONFLICT (code) DO UPDATE
               SET credits = EXCLUDED.credits,
                   limit_total = EXCLUDED.limit_total,
                   used_count = 0""",
            (code, credits, limit), commit=True)
        bot.reply_to(
            message,
            "✅ <b>ʀᴇᴅᴇᴇᴍ ɢᴇɴᴇʀᴀᴛᴇᴅ</b>\n"
            "━━━━━━━━━━━━━━━━━━\n"
            f"🎟 ᴄᴏᴅᴇ   : <code>{code}</code>\n"
            f"💰 ᴄʀᴇᴅɪᴛꜱ : <b>{credits}</b>\n"
            f"👥 ʟɪᴍɪᴛ   : <b>{limit}</b>",
            parse_mode="HTML"
        )
    except Exception:
        bot.reply_to(message,
            "⚠️ ᴜꜱᴀɢᴇ : <code>/redeem CODE CREDITS LIMIT</code>",
            parse_mode="HTML")

# ═══════════════════════════════════════════════════
#  CALLBACK: VERIFY JOIN
# ═══════════════════════════════════════════════════
@bot.callback_query_handler(func=lambda call: call.data == "verify_join")
def cb_verify_join(call):
    uid = call.from_user.id
    if banned_guard(uid):
        bot.answer_callback_query(call.id, "🚫 banned")
        return
    user = get_user(uid)
    if user['verified'] == 1:
        bot.answer_callback_query(call.id, "✅ ᴀʟʀᴇᴀᴅʏ ᴠᴇʀɪꜰɪᴇᴅ!")
        return
    if not get_main_channel():
        bot.answer_callback_query(call.id, "⚠️ ɴᴏ ᴄʜᴀɴɴᴇʟ ᴄᴏɴꜰɪɢᴜʀᴇᴅ.", show_alert=True)
        return
    set_verified(uid)
    bot.answer_callback_query(call.id, "🎉 ᴠᴇʀɪꜰɪᴇᴅ!")
    try:
        bot.edit_message_text(
            "🎉 <b>ᴠᴇʀɪꜰɪᴇᴅ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ</b>\n\n"
            "✅ ᴀᴄᴄᴇꜱꜱ ᴀᴄᴛɪᴠᴀᴛᴇᴅ. ᴇɴᴊᴏʏ!",
            call.message.chat.id, call.message.message_id,
            parse_mode="HTML")
    except Exception:
        pass
    bot.send_message(
        uid,
        "🏠 <b>ᴍᴀɪɴ ᴍᴇɴᴜ</b>\n\n👇 ᴄʜᴏᴏꜱᴇ ᴀɴ ᴏᴘᴛɪᴏɴ ʙᴇʟᴏᴡ.",
        reply_markup=main_menu_keyboard(uid),
        parse_mode="HTML"
    )

# ═══════════════════════════════════════════════════
#  ADMIN PANEL BUTTONS
# ═══════════════════════════════════════════════════
@bot.message_handler(func=lambda m: m.from_user.id in ADMIN_IDS and m.text == BTN_ADMIN)
def admin_panel_open(message):
    bot.send_message(
        message.chat.id,
        "🛠 <b>ᴀᴅᴍɪɴ ᴘᴀɴᴇʟ</b>\n"
        "━━━━━━━━━━━━━━━━━━\n\n"
        "ᴘɪᴄᴋ ᴀɴ ᴀᴄᴛɪᴏɴ ʙᴇʟᴏᴡ.",
        parse_mode="HTML",
        reply_markup=admin_panel_keyboard()
    )

# ── Broadcast ──
@bot.message_handler(func=lambda m: m.from_user.id in ADMIN_IDS and m.text == BTN_BROADCAST)
def admin_broadcast_start(message):
    msg = bot.send_message(
        message.chat.id,
        "📣 <b>ʙʀᴏᴀᴅᴄᴀꜱᴛ</b>\n"
        "━━━━━━━━━━━━━━━━━━\n\n"
        "ꜱᴇɴᴅ ᴛʜᴇ ᴍᴇꜱꜱᴀɢᴇ ᴛᴏ ʙʀᴏᴀᴅᴄᴀꜱᴛ.\n"
        "ᴛʏᴘᴇ <code>/back</code> ᴛᴏ ᴄᴀɴᴄᴇʟ.",
        parse_mode="HTML",
        reply_markup=telebot.types.ReplyKeyboardRemove()
    )
    bot.register_next_step_handler(msg, admin_broadcast_send)

def admin_broadcast_send(message):
    if message.from_user.id not in ADMIN_IDS:
        return
    if message.text and message.text.strip().lower() == "/back":
        bot.send_message(message.chat.id, "↩️ ᴄᴀɴᴄᴇʟʟᴇᴅ.",
                         reply_markup=admin_panel_keyboard())
        return
    rows = db_exec(
        """SELECT user_id FROM users
           WHERE user_id NOT IN (SELECT user_id FROM banned_users)""",
        fetch='all')
    ids = [r[0] for r in rows] if rows else []
    sent = failed = 0
    for uid in ids:
        try:
            bot.copy_message(uid, message.chat.id, message.message_id)
            sent += 1
        except Exception:
            failed += 1
    bot.send_message(
        message.chat.id,
        "📣 <b>ʙʀᴏᴀᴅᴄᴀꜱᴛ ᴄᴏᴍᴘʟᴇᴛᴇ</b>\n"
        "━━━━━━━━━━━━━━━━━━\n"
        f"✅ ꜱᴇɴᴛ   : <b>{sent}</b>\n"
        f"❌ ꜰᴀɪʟᴇᴅ : <b>{failed}</b>",
        parse_mode="HTML",
        reply_markup=admin_panel_keyboard()
    )

# ── Channels ──
@bot.message_handler(func=lambda m: m.from_user.id in ADMIN_IDS and m.text == BTN_CHANNELS)
def admin_channels_open(message):
    channel = get_main_channel() or "ɴᴏᴛ ᴄᴏɴꜰɪɢᴜʀᴇᴅ"
    bot.send_message(
        message.chat.id,
        f"📢 <b>ᴍᴀɴᴀɢᴇ ᴄʜᴀɴɴᴇʟꜱ</b>\n"
        f"━━━━━━━━━━━━━━━━━━\n\n"
        f"ᴄᴜʀʀᴇɴᴛ : <b>{clean_html(channel)}</b>",
        parse_mode="HTML",
        reply_markup=channels_manage_keyboard()
    )

@bot.callback_query_handler(func=lambda call: call.data in
                            {"admin_add_channel", "admin_remove_channel", "admin_panel_back"})
def cb_admin_channels(call):
    if call.from_user.id not in ADMIN_IDS:
        bot.answer_callback_query(call.id, "ᴀᴅᴍɪɴ ᴏɴʟʏ.", show_alert=True)
        return
    if call.data == "admin_add_channel":
        msg = bot.send_message(
            call.message.chat.id,
            "📢 ꜱᴇɴᴅ ᴄʜᴀɴɴᴇʟ ᴜꜱᴇʀɴᴀᴍᴇ ᴡɪᴛʜ <code>@</code>\n"
            "ᴛʏᴘᴇ <code>/back</code> ᴛᴏ ᴄᴀɴᴄᴇʟ.",
            parse_mode="HTML")
        bot.register_next_step_handler(msg, admin_save_channel)
    elif call.data == "admin_remove_channel":
        set_main_channel("")
        bot.answer_callback_query(call.id, "ᴄʜᴀɴɴᴇʟ ʀᴇᴍᴏᴠᴇᴅ")
        try:
            bot.edit_message_text("🗑 <b>ᴄʜᴀɴɴᴇʟ ʀᴇᴍᴏᴠᴇᴅ.</b>",
                                  call.message.chat.id,
                                  call.message.message_id,
                                  parse_mode="HTML")
        except Exception:
            pass
        bot.send_message(call.message.chat.id, "🛠 <b>ᴀᴅᴍɪɴ ᴘᴀɴᴇʟ</b>",
                         parse_mode="HTML",
                         reply_markup=admin_panel_keyboard())
    else:
        bot.answer_callback_query(call.id)
        try:
            bot.edit_message_text("🛠 <b>ᴀᴅᴍɪɴ ᴘᴀɴᴇʟ</b>",
                                  call.message.chat.id,
                                  call.message.message_id,
                                  parse_mode="HTML")
        except Exception:
            pass
        bot.send_message(call.message.chat.id, "🛠 <b>ᴀᴅᴍɪɴ ᴘᴀɴᴇʟ</b>",
                         parse_mode="HTML",
                         reply_markup=admin_panel_keyboard())

def admin_save_channel(message):
    if message.from_user.id not in ADMIN_IDS:
        return
    username = (message.text or "").strip()
    if username.lower() in {"/back", "back"}:
        bot.send_message(message.chat.id, "↩️ ᴄᴀɴᴄᴇʟʟᴇᴅ.",
                         reply_markup=admin_panel_keyboard())
        return
    if not username.startswith("@") or len(username) < 2 or " " in username:
        bot.send_message(
            message.chat.id,
            "⚠️ ꜱᴇɴᴅ ᴀ ᴠᴀʟɪᴅ ᴜꜱᴇʀɴᴀᴍᴇ ʟɪᴋᴇ <code>@YourChannel</code>",
            parse_mode="HTML",
            reply_markup=admin_panel_keyboard())
        return
    set_main_channel(username)
    bot.send_message(
        message.chat.id,
        f"✅ <b>ᴄʜᴀɴɴᴇʟ ꜱᴀᴠᴇᴅ</b>\n📢 {clean_html(username)}",
        parse_mode="HTML",
        reply_markup=admin_panel_keyboard())

# ── Add Balance ──
@bot.message_handler(func=lambda m: m.from_user.id in ADMIN_IDS and m.text == BTN_ADD_BAL)
def admin_add_balance_start(message):
    msg = bot.send_message(
        message.chat.id,
        "💰 <b>ᴀᴅᴅ ʙᴀʟᴀɴᴄᴇ</b>\n"
        "━━━━━━━━━━━━━━━━━━\n\n"
        "ꜱᴇɴᴅ : <code>user_id amount</code>\n"
        "ᴇxᴀᴍᴘʟᴇ : <code>123456789 25</code>\n\n"
        "ᴛʏᴘᴇ <code>/back</code> ᴛᴏ ᴄᴀɴᴄᴇʟ.",
        parse_mode="HTML",
        reply_markup=telebot.types.ReplyKeyboardRemove()
    )
    bot.register_next_step_handler(msg, admin_add_balance_do)

def admin_add_balance_do(message):
    if message.from_user.id not in ADMIN_IDS:
        return
    text = (message.text or "").strip()
    if text.lower() in {"/back", "back"}:
        bot.send_message(message.chat.id, "↩️ ᴄᴀɴᴄᴇʟʟᴇᴅ.",
                         reply_markup=admin_panel_keyboard())
        return
    try:
        parts = text.split()
        if len(parts) != 2:
            raise ValueError
        uid, amount = int(parts[0]), int(parts[1])
        if amount <= 0:
            raise ValueError
        get_user(uid)
        update_balance(uid, amount)
        new_bal = get_user(uid)['balance']
        bot.send_message(
            message.chat.id,
            f"✅ ᴀᴅᴅᴇᴅ <b>{amount}</b> ᴄʀᴇᴅɪᴛꜱ ᴛᴏ <code>{uid}</code>\n"
            f"💰 ᴜꜱᴇʀ ʙᴀʟᴀɴᴄᴇ : <b>{new_bal}</b>",
            parse_mode="HTML",
            reply_markup=admin_panel_keyboard())
    except Exception:
        bot.send_message(message.chat.id,
                         "⚠️ ꜰᴏʀᴍᴀᴛ : <code>user_id amount</code>",
                         parse_mode="HTML",
                         reply_markup=admin_panel_keyboard())

# ── Remove Balance ──
@bot.message_handler(func=lambda m: m.from_user.id in ADMIN_IDS and m.text == BTN_REM_BAL)
def admin_remove_balance_start(message):
    msg = bot.send_message(
        message.chat.id,
        "➖ <b>ʀᴇᴍᴏᴠᴇ ʙᴀʟᴀɴᴄᴇ</b>\n"
        "━━━━━━━━━━━━━━━━━━\n\n"
        "ꜱᴇɴᴅ : <code>user_id amount</code>\n"
        "ᴇxᴀᴍᴘʟᴇ : <code>123456789 10</code>\n\n"
        "ᴛʏᴘᴇ <code>/back</code> ᴛᴏ ᴄᴀɴᴄᴇʟ.",
        parse_mode="HTML",
        reply_markup=telebot.types.ReplyKeyboardRemove()
    )
    bot.register_next_step_handler(msg, admin_remove_balance_do)

def admin_remove_balance_do(message):
    if message.from_user.id not in ADMIN_IDS:
        return
    text = (message.text or "").strip()
    if text.lower() in {"/back", "back"}:
        bot.send_message(message.chat.id, "↩️ ᴄᴀɴᴄᴇʟʟᴇᴅ.",
                         reply_markup=admin_panel_keyboard())
        return
    try:
        parts = text.split()
        if len(parts) != 2:
            raise ValueError
        uid, amount = int(parts[0]), int(parts[1])
        if amount <= 0:
            raise ValueError
        user = get_user(uid)
        new_bal = max(0, user['balance'] - amount)
        set_balance(uid, new_bal)
        bot.send_message(
            message.chat.id,
            f"➖ ʀᴇᴍᴏᴠᴇᴅ <b>{amount}</b> ᴄʀᴇᴅɪᴛꜱ ꜰʀᴏᴍ <code>{uid}</code>\n"
            f"💰 ᴜꜱᴇʀ ʙᴀʟᴀɴᴄᴇ : <b>{new_bal}</b>",
            parse_mode="HTML",
            reply_markup=admin_panel_keyboard())
    except Exception:
        bot.send_message(message.chat.id,
                         "⚠️ ꜰᴏʀᴍᴀᴛ : <code>user_id amount</code>",
                         parse_mode="HTML",
                         reply_markup=admin_panel_keyboard())

# ── Ban User ──
@bot.message_handler(func=lambda m: m.from_user.id in ADMIN_IDS and m.text == BTN_BAN)
def admin_ban_start(message):
    msg = bot.send_message(
        message.chat.id,
        "🚫 <b>ʙᴀɴ ᴜꜱᴇʀ</b>\n"
        "━━━━━━━━━━━━━━━━━━\n\n"
        "ꜱᴇɴᴅ : <code>user_id [reason]</code>\n"
        "ᴇxᴀᴍᴘʟᴇ : <code>123456789 spam</code>\n\n"
        "ᴛʏᴘᴇ <code>/back</code> ᴛᴏ ᴄᴀɴᴄᴇʟ.",
        parse_mode="HTML",
        reply_markup=telebot.types.ReplyKeyboardRemove()
    )
    bot.register_next_step_handler(msg, admin_ban_do)

def admin_ban_do(message):
    if message.from_user.id not in ADMIN_IDS:
        return
    text = (message.text or "").strip()
    if text.lower() in {"/back", "back"}:
        bot.send_message(message.chat.id, "↩️ ᴄᴀɴᴄᴇʟʟᴇᴅ.",
                         reply_markup=admin_panel_keyboard())
        return
    try:
        parts = text.split(maxsplit=1)
        uid = int(parts[0])
        reason = parts[1] if len(parts) > 1 else "—"
        if uid in ADMIN_IDS:
            bot.send_message(message.chat.id, "❌ ᴄᴀɴ'ᴛ ʙᴀɴ ᴀɴ ᴀᴅᴍɪɴ.",
                             reply_markup=admin_panel_keyboard())
            return
        ban_user(uid, reason)
        try:
            bot.send_message(uid,
                "🚫 <b>ʏᴏᴜ ʜᴀᴠᴇ ʙᴇᴇɴ ʙᴀɴɴᴇᴅ ꜰʀᴏᴍ ᴛʜɪꜱ ʙᴏᴛ.</b>",
                parse_mode="HTML")
        except Exception:
            pass
        bot.send_message(
            message.chat.id,
            f"🚫 <b>ᴜꜱᴇʀ ʙᴀɴɴᴇᴅ</b>\n"
            f"🆔 <code>{uid}</code>\n"
            f"📝 ʀᴇᴀꜱᴏɴ : {clean_html(reason)}",
            parse_mode="HTML",
            reply_markup=admin_panel_keyboard())
    except Exception:
        bot.send_message(message.chat.id,
                         "⚠️ ꜰᴏʀᴍᴀᴛ : <code>user_id [reason]</code>",
                         parse_mode="HTML",
                         reply_markup=admin_panel_keyboard())

# ── Unban User ──
@bot.message_handler(func=lambda m: m.from_user.id in ADMIN_IDS and m.text == BTN_UNBAN)
def admin_unban_start(message):
    msg = bot.send_message(
        message.chat.id,
        "✅ <b>ᴜɴʙᴀɴ ᴜꜱᴇʀ</b>\n"
        "━━━━━━━━━━━━━━━━━━\n\n"
        "ꜱᴇɴᴅ : <code>user_id</code>\n"
        "ᴇxᴀᴍᴘʟᴇ : <code>123456789</code>\n\n"
        "ᴛʏᴘᴇ <code>/back</code> ᴛᴏ ᴄᴀɴᴄᴇʟ.",
        parse_mode="HTML",
        reply_markup=telebot.types.ReplyKeyboardRemove()
    )
    bot.register_next_step_handler(msg, admin_unban_do)

def admin_unban_do(message):
    if message.from_user.id not in ADMIN_IDS:
        return
    text = (message.text or "").strip()
    if text.lower() in {"/back", "back"}:
        bot.send_message(message.chat.id, "↩️ ᴄᴀɴᴄᴇʟʟᴇᴅ.",
                         reply_markup=admin_panel_keyboard())
        return
    try:
        uid = int(text.split()[0])
        unban_user(uid)
        try:
            bot.send_message(uid,
                "✅ <b>ʏᴏᴜ ʜᴀᴠᴇ ʙᴇᴇɴ ᴜɴʙᴀɴɴᴇᴅ.</b>",
                parse_mode="HTML")
        except Exception:
            pass
        bot.send_message(
            message.chat.id,
            f"✅ <b>ᴜꜱᴇʀ ᴜɴʙᴀɴɴᴇᴅ</b>\n🆔 <code>{uid}</code>",
            parse_mode="HTML",
            reply_markup=admin_panel_keyboard())
    except Exception:
        bot.send_message(message.chat.id,
                         "⚠️ ꜰᴏʀᴍᴀᴛ : <code>user_id</code>",
                         parse_mode="HTML",
                         reply_markup=admin_panel_keyboard())

# ═══════════════════════════════════════════════════
#  USER MENU (CATCH-ALL — MUST BE LAST)
# ═══════════════════════════════════════════════════
@bot.message_handler(func=lambda message: True)
def user_menu(message):
    uid = message.from_user.id
    if banned_guard(uid):
        return
    user = get_user(uid)
    text = (message.text or "").strip()

    if not is_owner(uid) and get_main_channel() and user['verified'] == 0:
        bot.send_message(
            uid,
            "🔐 <b>ᴘʟᴇᴀꜱᴇ ᴠᴇʀɪꜰʏ ꜰɪʀꜱᴛ.</b>\n\nᴊᴏɪɴ ᴛʜᴇ ᴄʜᴀɴɴᴇʟ, ᴛʜᴇɴ ᴛᴀᴘ ᴠᴇʀɪꜰʏ.",
            parse_mode="HTML",
            reply_markup=force_join_keyboard())
        return

    if text == BTN_BACK:
        bot.send_message(
            uid,
            "🏠 <b>ᴍᴀɪɴ ᴍᴇɴᴜ</b>",
            parse_mode="HTML",
            reply_markup=main_menu_keyboard(uid))
        return

    if text == BTN_SEARCH:
        bot.send_message(
            uid,
            "🔍 <b>ꜱᴇᴀʀᴄʜ ᴍᴇɴᴜ</b>\n"
            "━━━━━━━━━━━━━━━━━━\n\n"
            "ᴄʜᴏᴏꜱᴇ ᴀ ꜱᴇᴀʀᴄʜ ᴛʏᴘᴇ ʙᴇʟᴏᴡ.",
            parse_mode="HTML",
            reply_markup=search_menu_keyboard(uid))
        return

    if text == BTN_S_NUM:
        if not is_owner(uid) and user['balance'] < 1:
            bot.send_message(uid,
                "❌ <b>ɪɴꜱᴜꜰꜰɪᴄɪᴇɴᴛ ʙᴀʟᴀɴᴄᴇ!</b>",
                parse_mode="HTML",
                reply_markup=search_menu_keyboard(uid))
            return
        msg = bot.send_message(uid,
            "📱 ꜱᴇɴᴅ 10 ᴅɪɢɪᴛ ᴍᴏʙɪʟᴇ ɴᴜᴍʙᴇʀ :",
            reply_markup=telebot.types.ReplyKeyboardRemove())
        bot.register_next_step_handler(msg, process_num_info)
        return

    if text == BTN_S_AADHAAR:
        if not is_owner(uid) and user['balance'] < 1:
            bot.send_message(uid,
                "❌ <b>ɪɴꜱᴜꜰꜰɪᴄɪᴇɴᴛ ʙᴀʟᴀɴᴄᴇ!</b>",
                parse_mode="HTML",
                reply_markup=search_menu_keyboard(uid))
            return
        msg = bot.send_message(uid,
            "🆔 ꜱᴇɴᴅ 12 ᴅɪɢɪᴛ ᴀᴀᴅʜᴀᴀʀ ɴᴜᴍʙᴇʀ :",
            reply_markup=telebot.types.ReplyKeyboardRemove())
        bot.register_next_step_handler(msg, process_aadhaar_info)
        return

    if text == BTN_BALANCE:
        bot.send_message(
            uid,
            f"💰 <b>ʏᴏᴜʀ ʙᴀʟᴀɴᴄᴇ</b>\n"
            f"━━━━━━━━━━━━━━━━━━\n\n"
            f"💳 ᴄʀᴇᴅɪᴛꜱ : <b>{balance_text(uid)}</b>",
            parse_mode="HTML",
            reply_markup=main_menu_keyboard(uid))

    elif text == BTN_REDEEM:
        msg = bot.send_message(uid,
            "🎁 ꜱᴇɴᴅ ʀᴇᴅᴇᴇᴍ ᴄᴏᴅᴇ.\nᴛʏᴘᴇ <code>/back</code> ᴛᴏ ᴀʙᴏʀᴛ.",
            parse_mode="HTML",
            reply_markup=telebot.types.ReplyKeyboardRemove())
        bot.register_next_step_handler(msg, process_redeem)

    elif text == BTN_OWNER:
        bot.send_message(uid, OWNER_TEXT,
                         parse_mode="HTML",
                         reply_markup=main_menu_keyboard(uid))

    else:
        bot.send_message(
            uid,
            "🏠 <b>ᴍᴀɪɴ ᴍᴇɴᴜ</b>\n\n👇 ᴄʜᴏᴏꜱᴇ ᴀɴ ᴏᴘᴛɪᴏɴ ʙᴇʟᴏᴡ.",
            parse_mode="HTML",
            reply_markup=main_menu_keyboard(uid))

# ═══════════════════════════════════════════════════
#  NUM INFO FLOW
# ═══════════════════════════════════════════════════
def process_num_info(message):
    uid = message.from_user.id
    if banned_guard(uid):
        return
    num = (message.text or "").strip()

    if num.lower() == "back" or num == "/back":
        bot.send_message(uid, "↩️ ᴀʙᴏʀᴛᴇᴅ.",
                         reply_markup=search_menu_keyboard(uid))
        return

    user = get_user(uid)
    if not is_owner(uid) and user['balance'] < 1:
        bot.send_message(uid,
            "❌ <b>ɪɴꜱᴜꜰꜰɪᴄɪᴇɴᴛ ʙᴀʟᴀɴᴄᴇ!</b>",
            parse_mode="HTML",
            reply_markup=search_menu_keyboard(uid))
        return

    if not num.isdigit() or len(num) != 10:
        bot.send_message(uid,
            "⚠️ ɪɴᴠᴀʟɪᴅ ꜰᴏʀᴍᴀᴛ! ꜱᴇɴᴅ ᴇxᴀᴄᴛʟʏ 10 ᴅɪɢɪᴛꜱ.",
            reply_markup=search_menu_keyboard(uid))
        return

    wait = bot.send_message(uid, "⏳ ꜰᴇᴛᴄʜɪɴɢ ᴅᴇᴛᴀɪʟꜱ, ᴘʟᴇᴀꜱᴇ ᴡᴀɪᴛ...")

    try:
        res = requests.get(API_NUM.format(num=num), timeout=15).json()
    except Exception:
        try:
            bot.edit_message_text("⚠️ <b>ᴀᴘɪ ᴇʀʀᴏʀ.</b>",
                                  wait.chat.id, wait.message_id,
                                  parse_mode="HTML")
        except Exception:
            pass
        bot.send_message(uid, "👇 ᴄʜᴏᴏꜱᴇ ᴀɴ ᴏᴘᴛɪᴏɴ ʙᴇʟᴏᴡ.",
                         reply_markup=search_menu_keyboard(uid))
        return

    d = extract_first_data(res)
    if d is None:
        try:
            bot.edit_message_text("❌ <b>ɴᴏ ᴅᴀᴛᴀ ꜰᴏᴜɴᴅ.</b>",
                                  wait.chat.id, wait.message_id,
                                  parse_mode="HTML")
        except Exception:
            pass
        bot.send_message(uid, "👇 ᴄʜᴏᴏꜱᴇ ᴀɴ ᴏᴘᴛɪᴏɴ ʙᴇʟᴏᴡ.",
                         reply_markup=search_menu_keyboard(uid))
        return

    if not is_owner(uid):
        update_balance(uid, -1)

    tail = ("💰 <b>ᴏᴡɴᴇʀ : ᴜɴʟɪᴍɪᴛᴇᴅ</b>"
            if is_owner(uid)
            else f"💰 1 ᴄʀᴇᴅɪᴛ ᴅᴇᴅᴜᴄᴛᴇᴅ • ʀᴇᴍᴀɪɴɪɴɢ : <b>{get_user(uid)['balance']}</b>")

    text = (
        "✅ <b>ɴᴜᴍʙᴇʀ ᴅᴇᴛᴀɪʟꜱ ꜰᴏᴜɴᴅ</b>\n"
        "━━━━━━━━━━━━━━━━━━\n"
        f"📱 <b>ᴍᴏʙɪʟᴇ</b>      : <code>{clean_html(d.get('mobile'))}</code>\n"
        f"🫵 <b>ɴᴀᴍᴇ</b>        : <code>{clean_html(d.get('name'))}</code>\n"
        f"👨‍👦 <b>ꜰᴀᴛʜᴇʀ</b>      : <code>{clean_html(d.get('father_name'))}</code>\n"
        f"🏠 <b>ᴀᴅᴅʀᴇꜱꜱ</b>     : <code>{clean_html(d.get('address'))}</code>\n"
        f"📞 <b>ᴀʟᴛ ᴍᴏʙɪʟᴇ</b>  : <code>{clean_html(d.get('alt_mobile'))}</code>\n"
        f"🌐 <b>ᴄɪʀᴄʟᴇ</b>      : <code>{clean_html(d.get('circle'))}</code>\n"
        "━━━━━━━━━━━━━━━━━━\n"
        + tail
    )
    try:
        bot.edit_message_text(text, wait.chat.id, wait.message_id, parse_mode="HTML")
    except Exception:
        try:
            bot.send_message(uid, text, parse_mode="HTML")
        except Exception:
            pass
    bot.send_message(uid, "👇 ᴄʜᴏᴏꜱᴇ ᴀɴ ᴏᴘᴛɪᴏɴ ʙᴇʟᴏᴡ.",
                     reply_markup=search_menu_keyboard(uid))

# ═══════════════════════════════════════════════════
#  AADHAAR INFO FLOW
# ═══════════════════════════════════════════════════
def process_aadhaar_info(message):
    uid = message.from_user.id
    if banned_guard(uid):
        return
    aadhar = (message.text or "").strip()

    if aadhar.lower() == "back" or aadhar == "/back":
        bot.send_message(uid, "↩️ ᴀʙᴏʀᴛᴇᴅ.",
                         reply_markup=search_menu_keyboard(uid))
        return

    user = get_user(uid)
    if not is_owner(uid) and user['balance'] < 1:
        bot.send_message(uid,
            "❌ <b>ɪɴꜱᴜꜰꜰɪᴄɪᴇɴᴛ ʙᴀʟᴀɴᴄᴇ!</b>",
            parse_mode="HTML",
            reply_markup=search_menu_keyboard(uid))
        return

    if not aadhar.isdigit() or len(aadhar) != 12:
        bot.send_message(uid,
            "⚠️ ɪɴᴠᴀʟɪᴅ ꜰᴏʀᴍᴀᴛ! ꜱᴇɴᴅ ᴇxᴀᴄᴛʟʏ 12 ᴅɪɢɪᴛꜱ.",
            reply_markup=search_menu_keyboard(uid))
        return

    wait = bot.send_message(uid, "⏳ ꜰᴇᴛᴄʜɪɴɢ ᴀᴀᴅʜᴀᴀʀ ᴅᴇᴛᴀɪʟꜱ, ᴘʟᴇᴀꜱᴇ ᴡᴀɪᴛ...")

    try:
        res = requests.get(API_AADHAAR.format(aadhar_id=aadhar), timeout=20).json()
    except Exception:
        try:
            bot.edit_message_text("⚠️ <b>ᴀᴘɪ ᴇʀʀᴏʀ.</b>",
                                  wait.chat.id, wait.message_id,
                                  parse_mode="HTML")
        except Exception:
            pass
        bot.send_message(uid, "👇 ᴄʜᴏᴏꜱᴇ ᴀɴ ᴏᴘᴛɪᴏɴ ʙᴇʟᴏᴡ.",
                         reply_markup=search_menu_keyboard(uid))
        return

    d = extract_first_data(res)
    if d is None:
        try:
            bot.edit_message_text("❌ <b>ɴᴏ ᴅᴀᴛᴀ ꜰᴏᴜɴᴅ.</b>",
                                  wait.chat.id, wait.message_id,
                                  parse_mode="HTML")
        except Exception:
            pass
        bot.send_message(uid, "👇 ᴄʜᴏᴏꜱᴇ ᴀɴ ᴏᴘᴛɪᴏɴ ʙᴇʟᴏᴡ.",
                         reply_markup=search_menu_keyboard(uid))
        return

    if not is_owner(uid):
        update_balance(uid, -1)

    tail = ("💰 <b>ᴏᴡɴᴇʀ : ᴜɴʟɪᴍɪᴛᴇᴅ</b>"
            if is_owner(uid)
            else f"💰 1 ᴄʀᴇᴅɪᴛ ᴅᴇᴅᴜᴄᴛᴇᴅ • ʀᴇᴍᴀɪɴɪɴɢ : <b>{get_user(uid)['balance']}</b>")

    text = format_aadhaar(d) + "\n━━━━━━━━━━━━━━━━━━\n" + tail
    try:
        bot.edit_message_text(text, wait.chat.id, wait.message_id, parse_mode="HTML")
    except Exception:
        try:
            bot.send_message(uid, text, parse_mode="HTML")
        except Exception:
            pass
    bot.send_message(uid, "👇 ᴄʜᴏᴏꜱᴇ ᴀɴ ᴏᴘᴛɪᴏɴ ʙᴇʟᴏᴡ.",
                     reply_markup=search_menu_keyboard(uid))

# ═══════════════════════════════════════════════════
#  REDEEM FLOW
# ═══════════════════════════════════════════════════
def process_redeem(message):
    uid = message.from_user.id
    if banned_guard(uid):
        return
    code_input = (message.text or "").strip().upper()

    if code_input.lower() == "back" or code_input == "/BACK":
        bot.send_message(uid, "↩️ ᴀʙᴏʀᴛᴇᴅ.",
                         reply_markup=main_menu_keyboard(uid))
        return

    already = db_exec(
        "SELECT 1 FROM redeemed_by WHERE user_id = %s AND code = %s",
        (uid, code_input), fetch='one')
    if already:
        bot.send_message(uid, "⚠️ ᴀʟʀᴇᴀᴅʏ ʀᴇᴅᴇᴇᴍᴇᴅ.",
                         reply_markup=main_menu_keyboard(uid))
        return

    row = db_exec(
        "SELECT code, credits, limit_total, used_count FROM redeem_codes WHERE code = %s",
        (code_input,), fetch='one')
    if not row:
        bot.send_message(uid, "❌ ɪɴᴠᴀʟɪᴅ ᴄᴏᴅᴇ.",
                         reply_markup=main_menu_keyboard(uid))
        return

    _, credits, limit_total, used = row
    if used >= limit_total:
        bot.send_message(uid, "❌ ᴛʜɪꜱ ᴄᴏᴅᴇ ʜᴀꜱ ᴇxᴘɪʀᴇᴅ.",
                         reply_markup=main_menu_keyboard(uid))
        return

    try:
        db_exec(
            "UPDATE redeem_codes SET used_count = used_count + 1 WHERE code = %s",
            (code_input,), commit=True)
        db_exec(
            "INSERT INTO redeemed_by (user_id, code) VALUES (%s, %s)",
            (uid, code_input), commit=True)
    except Exception:
        bot.send_message(uid, "⚠️ ʀᴇᴅᴇᴇᴍ ꜰᴀɪʟᴇᴅ. ᴛʀʏ ᴀɢᴀɪɴ.",
                         reply_markup=main_menu_keyboard(uid))
        return

    update_balance(uid, credits)
    bot.send_message(
        uid,
        f"🎉 <b>ʀᴇᴅᴇᴇᴍ ꜱᴜᴄᴄᴇꜱꜱ</b>\n"
        f"━━━━━━━━━━━━━━━━━━\n"
        f"➕ <b>+{credits}</b> ᴄʀᴇᴅɪᴛꜱ ᴀᴅᴅᴇᴅ\n"
        f"💰 ɴᴇᴡ ʙᴀʟᴀɴᴄᴇ : <b>{balance_text(uid)}</b>",
        parse_mode="HTML",
        reply_markup=main_menu_keyboard(uid))

# ═══════════════════════════════════════════════════
#  RUN
# ═══════════════════════════════════════════════════
if __name__ == "__main__":
    print("Bot is running...")
    bot.infinity_polling(timeout=30, long_polling_timeout=30)