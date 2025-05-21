def draw_stars(N: int)-> list:
    if N == 1:
        return ['*']
    
    stars = draw_stars(N // 3)
    
    L = []
    for star in stars:
        L.append(star * 3)
    for star in stars:
        L.append(star + ' ' * (N // 3)+ star)
    for star in stars:
        L.append(star * 3)

    return L

N = int(input())
print("\n".join(draw_stars(N)))