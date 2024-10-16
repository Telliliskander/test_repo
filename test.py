########### ahmed program ##############

liste_1 = [1,5,6,4,3]

liste_2 = [1,2,5,1,3]

l_1 = len(liste_1)
l_2 = len(liste_2)

s_1 = 0
s_2 = 0


for i in range(l_1): # range(l_1) = [0,1,2,3,4]    
    
    s_1 = s_1 + liste_1[i]
    s_2 = s_2 + liste_2[i]

if s_1 > s_2 : 
    print("Joueur 1 gagnant")
elif  s_1 < s_2 : 
    print("Joueur 2 gagnant")
elif s_1 == s_2: 
    print("le match est nul")


print(s_1)
print(s_2)
    


    

