from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8600265043:AAFK2SiRNlndEpbc3jneirUii0LhDT-XICY"
LINK_GRUPO = "t.me/tpggratis"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    nome = update.effective_user.first_name

    mensagem1 = (
        f"🎉 Olá {nome}, bem-vindo ao TPG ZeroLoss!\n\n"
        "🎁 ATENÇÃO: SINAL GRATUITO DISPONÍVEL!\n\n"
        "Para receber seu sinal FREE agora mesmo, você precisa estar no grupo. "
        "É lá que todos os sinais chegam em tempo real!\n\n"
        "👇👇👇 É SÓ CLICAR NO BOTÃO VERDE AQUI EMBAIXO 👇👇👇"
    )

    botao = InlineKeyboardMarkup([
        [InlineKeyboardButton("✅ ENTRAR NO GRUPO AGORA", url=LINK_GRUPO)]
    ])

    await update.message.reply_text(mensagem1, reply_markup=botao)

    await update.message.reply_text(
        f"🏆 Parabéns {nome}! Seja muito bem-vindo ao TPG ZeroLoss!\n\n"
        "Você acaba de dar o primeiro passo rumo aos melhores sinais! 🚀🔥"
    )

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()
