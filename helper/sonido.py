# -*- coding: utf-8 -*-
import winsound
import time
def alerta_sonora(idx,riesgo):
    path = r'sounds/'
    audio=['adenosina.wav', 'adrenalina.wav', 'aminofilina.wav', 'amiodarona.wav', 'aspirina 500mg.wav', 'sounds/atropina.wav', 'betametasona.wav', 'bicarbonato de sodio.wav', 'cedilanid.wav', 'diazepam.wav', 'dopamina.wav', 'efedrina.wav', 'fenitoína.wav', 'flumazenilo.wav', 'flurosemida.wav', 'gluconato de calcio.wav', 'glucosa 30%.wav', 'heparina.wav', 'hidrocortisona.wav', 'isoproterenol.wav', 'labetalol.wav', 'lidocaina.wav', 'midazolam.wav', 'naloxona.wav', 'nitroglicerina.wav', 'norepinefrina.wav', 'plavix 300mg.wav', 'propranolol 100mg.wav', 'sulfato de magnesio.wav', 'varepamilo.wav']
    audioPath = path + audio[idx]
    try:
        winsound.PlaySound(audioPath,winsound.SND_ASYNC)
        time.sleep(1.9)
    except:
        print('\nMedicamento sin registro de audio')
    if riesgo[idx]=='Alto':
        winsound.PlaySound(path+'riesgo.wav',winsound.SND_ASYNC)
        time.sleep(1.5)