import edge_tts
import asyncio

class TextToSpeech:
    def __init__(self, voice="pt-BR-AntonioNeural"):
        """
        :param voice: Voz desejada (consulte a lista de vozes com `edge-tts list-voices`).
        """
        self.voice = voice

    async def synthesize_speech_async(self, text, output_file):
        """
        Gera áudio de forma assíncrona (use em ambientes async).
        """
        communicate = edge_tts.Communicate(text, self.voice)
        await communicate.save(output_file)
        print(f"Áudio salvo em: {output_file}")

    def synthesize_speech(self, text, output_file):
        """
        Versão síncrona para uso geral.
        """
        asyncio.run(self.synthesize_speech_async(text, output_file))



# Teste de uso:

"""if __name__ == "__main__":
    tts = TextToSpeech()
    tts.synthesize_speech("Olá, mundo! Este áudio foi gerado pelo Edge TTS.", "saida.mp3")

# Versão assíncrona (em corrotinas):
async def main():
    await tts.synthesize_speech_async("Oi chefe, após uma analise de vendas de 2024, é com prazer que posso apresentar que o melhor vendedor de 2024 foi brenda duarte", "saida.mp3")

asyncio.run(main())"""