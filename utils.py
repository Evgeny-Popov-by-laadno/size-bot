def calculate_size(category, height, weight):
    """
    Подбор размера на основе таблицы.
    
    Таблица (исправленная):
      XS:  рост до 158,   вес 41–62
      S:   рост 158–168,  вес 50–62
      M:   рост 158–178,  вес 50–73
      L:   рост 168–178,  вес 62–73
      XL:  рост 178–188,  вес 73–88
      XXL: рост 178–188,  вес 104–120
    """
    
    size_table = [
        (0,   158,  41,  62,  "XS"),
        (158, 168,  50,  62,  "S"),
        (158, 178,  50,  73,  "M"),
        (168, 178,  62,  73,  "L"),
        (178, 188,  73,  88,  "XL"),
        (178, 188, 104, 120,  "XXL"),
    ]
    
    # Ищем точное совпадение
    for min_h, max_h, min_w, max_w, size in size_table:
        if min_h <= height <= max_h and min_w <= weight <= max_w:
            return size
    
    # Если точного совпадения нет — ищем ближайший размер
    best_size = "M"
    best_score = 9999
    
    for min_h, max_h, min_w, max_w, size in size_table:
        score = 0
        
        if height < min_h:
            score += (min_h - height) * 2
        elif height > max_h:
            score += (height - max_h) * 2
            
        if weight < min_w:
            score += (min_w - weight) * 3
        elif weight > max_w:
            score += (weight - max_w) * 3
        
        if score < best_score:
            best_score = score
            best_size = size
    
    return best_size