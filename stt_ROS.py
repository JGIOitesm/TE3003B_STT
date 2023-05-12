from time import sleep

import rospy
import speech_recognition as sr

import control_uav


def main():
    r = sr.Recognizer()
    rospy.init_node("DRONE_GEORGE")
    sleep(2)

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Escuchando...")
        while True:
            audio = r.listen(source, 5, 3)
            try:
                text = r.recognize_google(audio, language="es-MX")
                text = text.lower() + "."
                print(text)
                if text == "levántate.":
                    control_uav.setMode("GUIDED")
                    sleep(2)
                    control_uav.setArm()
                    sleep(2)
                    control_uav.setTakeofMode()
                    sleep(5)
                    print("Escuchando...")
                if text == "siéntate.":
                    control_uav.setLandMode()
                    sleep(15)
                    print("Escuchando...")
                if text == "adiós.":
                    break
            except sr.UnknownValueError:
                print("Esperando dictado...")


if __name__ == "__main__":
    try:
        main()
    except rospy.ROSInterruptException:
        pass
