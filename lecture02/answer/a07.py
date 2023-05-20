"""
1. 아래 lyrics_words는 dynamite-BTS의 가사를 단어 단위로 쪼개놓은 리스트이다.
2. 그렇기 때문에 중복된 단어가 여러번 들어가 있을 수 있는데,
3. 각 단어들이 몇번씩 들어가있는지, 저장하는 dictionary를 만들고 print 한다.
4. ex: my_dict = { Cause: 2, I: 3, ... }
"""

lyrics_words = ['Cause', 'I', 'I', 'Im', 'in', 'the', 'stars', 'tonight', 'So', 'watch', 'me', 'bring', 'the', 'fire', 'and', 'set', 'the', 'night', 'alight', 'Shoes', 'on', 'get', 'up', 'in', 'the', 'morn', 'Cup', 'of', 'milk', 'lets', 'rock', 'and', 'roll', 'King', 'Kong', 'kick', 'the', 'drum', 'rolling', 'on', 'like', 'a', 'Rolling', 'Stone', 'Sing', 'song', 'when', 'Im', 'walking', 'home', 'Jump', 'up', 'to', 'the', 'top', 'LeBron', 'Ding', 'dong', 'call', 'me', 'on', 'my', 'phone', 'Ice', 'tea', 'and', 'a', 'game', 'of', 'ping', 'pong', 'huh', 'This', 'is', 'getting', 'heavy', 'Can', 'you', 'hear', 'the', 'bass', 'boom?', 'Im', 'ready', 'woo', 'hoo', 'Life', 'is', 'sweet', 'as', 'honey', 'Yeah', 'this', 'beat', 'cha', 'ching', 'like', 'money', 'huh', 'Disco', 'overload', 'Im', 'into', 'that', 'Im', 'good', 'to', 'go', 'Im', 'diamond', 'you', 'know', 'I', 'glow', 'up', 'Hey', 'so', 'lets', 'go', 'Cause', 'I', 'I', 'Im', 'in', 'the', 'stars', 'tonight', 'So', 'watch', 'me', 'bring', 'the', 'fire', 'and', 'set', 'the', 'night', 'alight', 'hey', 'Shining', 'through', 'the', 'city', 'with', 'a', 'little', 'funk', 'and', 'soul', 'So', 'Ima', 'light', 'it', 'up', 'like', 'dynamite', 'whoa', 'oh', 'oh', 'Bring', 'a', 'friend', 'join', 'the', 'crowd', 'Whoever', 'wanna', 'come', 'along', 'Word', 'up', 'talk', 'the', 'talk', 'Just', 'move', 'like', 'we', 'off', 'the', 'wall', 'Day', 'or', 'night', 'the', 'skys', 'alight', 'So', 'we', 'dance', 'to', 'the', 'break', 'of', 'dawn', 'hey', 'Ladies', 'and', 'gentlemen', 'I', 'got', 'the', 'medicine', 'So', 'you', 'should', 'keep', 'ya', 'eyes', 'on', 'the', 'ball', 'huh', 'This', 'is', 'getting', 'heavy', 'Can', 'you', 'hear', 'the', 'bass', 'boom?', 'Im', 'ready', 'woo', 'hoo', 'Life', 'is', 'sweet', 'as', 'honey', 'Yeah', 'this', 'beat', 'cha', 'ching', 'like', 'money', 'Disco', 'overload', 'Im', 'into', 'that', 'Im', 'good', 'to', 'go', 'Im', 'diamond', 'you', 'know', 'I', 'glow', 'up', 'Lets', 'go', 'Cause', 'I', 'I', 'Im', 'in', 'the', 'stars', 'tonight', 'So', 'watch', 'me', 'bring', 'the', 'fire', 'and', 'set', 'the', 'night', 'alight', 'hey', 'Shining', 'through', 'the', 'city', 'with', 'a', 'little', 'funk', 'and', 'soul', 'So', 'Ima', 'light', 'it', 'up', 'like', 'dynamite', 'whoa', 'oh', 'oh', 'Dy', 'na', 'na', 'na', 'na', 'na', 'na', 'na', 'na', 'na', 'na', 'na', 'life', 'is', 'dynamite', 'Dy', 'na', 'na', 'na', 'na', 'na', 'na', 'na', 'na', 'na', 'na', 'na', 'life', 'is', 'dynamite', 'Shining', 'through', 'the', 'city', 'with', 'a', 'little', 'funk', 'and', 'soul', 'So', 'Ima', 'light', 'it', 'up', 'like', 'dynamite', 'whoa', 'oh', 'oh', 'Dy', 'na', 'na', 'na', 'na', 'na', 'na', 'na', 'ayy', 'Dy', 'na', 'na', 'na', 'na', 'na', 'na', 'na', 'ayy', 'Dy', 'na', 'na', 'na', 'na', 'na', 'na', 'na', 'ayy', 'Light', 'it', 'up', 'like', 'dynamite', 'Dy', 'na']

lyrics_dict = {}

for word in  lyrics_words:
    if word in lyrics_dict:
        lyrics_dict[word] += 1
    else:
        lyrics_dict[word] = 1

print(lyrics_dict)