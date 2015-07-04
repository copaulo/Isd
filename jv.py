from random import choice
import time     
class JogoDaVelha:
    vez = None
    jogo = [None for i in range(9)]
    def __init__(self,jog1,jog2):
        self._wait = 1
        self.jog1 = jog1
        self.jog2 = jog2
        self.vez = self.jog1
        if jog1.startswith('com') and jog2.startswith('com'):
            self._wait = 0
        self.inicio()
        
    def printGame(self,pgame=None):
        jogo = self.jogo
        for i in range(0,9,3):
            a,b,c = [(jogo[i+k] if jogo[i+k]!=None else i+k) for k in (0,1,2)]
            print('{} {} {}'.format(a,b,c))
            
    def isValidChoice(self,op):
        return 0<=op<=8 and self.jogo[op]==None
        
    def getOp(self):
        vez = self.vez
        if vez[:3]!='com':
            while True:
                print('\n\nEscolha Uma opção!\nJogo Atual:\n')
                self.printGame([i for i in range(9)])
                op = int(input('\nEscolha uma Opção {}: '.format(vez)))
                if self.isValidChoice(op):
                    print('ok',op)
                    return op
                print('\n\n\nJogada Invalida')
                time.sleep(1)
        else:
            if self._wait:
                print('{} Jogou'.format(vez))
                time.sleep(1)
            op = self.getIAOp()
            return op
            
    def getIAOp(self):
        '''
prioridade 1 -> possibilidade de vitoria
prioridade 2 -> possibilidade de derrota
prioridade 3 -> armar jogada
prioridade 4 -> desmanchar jogada do adv.
prioridade 5 -> jogada aleatoria'''
        
        mym = 'X' if self.jog1=='com' else 'O'
        otm = 'X' if mym=='O' else 'O'
        all_plays = [(0,1,2),(3,4,5),(6,7,8),
                     (0,3,6),(1,4,7),(2,5,8),
                     (0,4,8),(2,4,6)]
        
        def _hasRisc(play,game,tp,t):
            o = []
            for i in play:
                if game[i] != tp:
                    o.append(i)
            if len(o)==3-t:
                o = [i for i in o if self.isValidChoice(i)]
                if t==1:
                    for i in play:
                        a = 'X' if tp == 'O' else 'X'
                        if game[i] == a: return None
                if not len(o):
                    return None
                return choice(o)
            return None
       
        for play in all_plays:#prioridade 1
            x = _hasRisc(play,self.jogo,mym,2)
            if x!=None:
                return x
        for play in all_plays:#prioridade 2
            x = _hasRisc(play,self.jogo,otm,2)
            if x!=None:
                return x
        for play in all_plays:#prioridade 3
            x = _hasRisc(play,self.jogo,mym,1)
            if x!=None:
                return x
        for play in all_plays:#prioridade 4
            x = _hasRisc(play,self.jogo,otm,1)
            if x!=None:
                return x
        x = [i for i in range(9) if self.isValidChoice(i)]#prioridade 5
        return choice(x)
            
        
    def inicio(self):
        while True:
            op = self.getOp()
            if self.vez == self.jog1:
                self.jogo[op] = 'X'
                self.vez = self.jog2
            else:
                self.jogo[op] = 'O'
                self.vez = self.jog1
            if self.checkGame():
                print('Final de Jogo:')
                self.printGame()
                return
    def checkGame(self):
        empate = True
        for i in self.jogo:
            if i==None:
                empate = False
        if empate:
            print('Ninguem Venceu!')
            return True
            
        all_plays = [(0,1,2),(3,4,5),(6,7,8),
                     (0,3,6),(1,4,7),(2,5,8),
                     (0,4,8),(2,4,6)]
        def _allEquals(play,game):
            s = game[play[0]]
            s = [game[i] for i in play if game[i]==s]
            if None in s: return False,0
            return len(s)==3,s[0]
        for play in all_plays:
            x,y = _allEquals(play,self.jogo)
            if x:
                v = self.jog1 if y == 'X' else self.jog2
                print('Jogador {} Venceu!!!'.format(v))
                return True
        return False
    
#print('Jogador Vs Jogador')
#JogoDaVelha('Paulo','Pedro')
print('Jogador Vs IA')
JogoDaVelha('Ricardo','com1')
#print('IA Vs IA')
#JogoDaVelha('com1','com2')
            



        
    
