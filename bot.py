from telegram.ext import Updater,CommandHandler, Filters, MessageHandler
tasks=[]

def init(lista):
    fIn = open("task_list.txt","r")
    testo=fIn.read()
    fIn.close()
    lista=testo.split("\n")
    return lista

def stampa(bot,update):
    if len(tasks) == 0:
        testo="No tasks left!"
    else:
        testo = ""
        for elem in tasks:
            testo = testo + elem +"\n"
    update.message.reply_text(testo)
    return

def scrivi():
    fOut = open("task_list.txt","w")
    c=1
    N=len(tasks)
    for elem in tasks:
        if c!=N:
            fOut.write(elem + "\n")
        else:
            fOut.write(elem)
        c=c+1
    fOut.close()
    return

def nuovo(bot,update,args):
    str = ""
    c=0
    for pezzo in args:
        if c==0:
            str=pezzo
        else:
            str = str + " " + pezzo
        c=c+1
    tasks.append(str)
    #print(tasks)
    scrivi()
    update.message.reply_text("Added one element.")
    return

def removeOne(bot,update,args):
    str = ""
    c=0
    for pezzo in args:
        if (c==0):
            str=pezzo
        else:
            str = str + " " + pezzo
        c=c+1
    if str in tasks:
        tasks.remove(str)
        scrivi()
        update.message.reply_text("Rimosso l'elemento.")
    else:
        update.message.reply_text("Not found.")
    return

def removeAll(bot,update,args):
    str = ""
    c=0
    for pezzo in args:
        if c==0:
            str=pezzo
        else:
            str = str+ " " + pezzo
        c=c+1
    print(str)
    c=0
    eliminati=[]
    print(tasks)
    for elem in tasks:
        print(elem,end=' ')
        flag = elem.find(str)
        if flag>0:
            print("maggiore")
        else:
            print("minore")
        if flag>=0:
            eliminati.append(elem)
            tasks.remove(elem)
            c=c+1
    #print("test")
    if c==0:
        update.message.reply_text("No elements with that substring.")
    else:
        scrivi()
        str=str(eliminati)
        update.message.reply_text("The following were eliminated:\n" + str)
    return


def start(bot,update):
    update.message.reply_text("Bonaaaa!")
    return
def fine(bot,update):
    update.message.reply_text("Addio")
    exit(1)

def errore(bot,update):
    update.message.reply_text("This is not a valid command.")
    return

def main():
    updater = Updater("567551135:AAFJWKVZ8JS0raa_cVQa4c0GoOkTep1cK8k")
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start",start))
    dispatcher.add_handler(CommandHandler("end",fine))
    dispatcher.add_handler(CommandHandler("showTasks",stampa))
    dispatcher.add_handler(CommandHandler("removeTask",removeOne,pass_args=True))
    dispatcher.add_handler(CommandHandler("removeAll",removeAll,pass_args=True))
    dispatcher.add_handler(CommandHandler("newTask",nuovo,pass_args=True))
    dispatcher.add_handler(MessageHandler(Filters.text,errore))
    updater.start_polling()
    updater.idle()
    return


if __name__=='__main__':
    tasks = init(tasks)
    main()