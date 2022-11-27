batch_size = 100
img_width, img_height, img_num_channels = 32, 32, 3
input_shape = (32, 32, 3)
img_size = (1, 32, 32, 3)
optimizer = 'adam'
loss_function = 'sparse_categorical_crossentropy'
metrics = 'accuracy'
activation_r = 'relu'
activation_s = 'softmax'
classes = 100
epochs = 10
name_class = ['Beaver', 'Dolphin', 'Otter', 'Seal', 'Whale', 'Aquarium fish', 'Flatfish', 'Ray', 'Shark', 'Trout', 'Orchids',  'Poppies',
              'Roses', 'Sunflower', 'Tulips', 'Bottles', 'Bowls', 'Cans', 'Cups', 'Plates', 'Apples', 'Mushrooms', 'Oranges', 'Pears',
              'Sweet peppers', 'Clok', 'Computer keyboard', 'Lamp', 'Telephone', 'Television', 'Bed', 'Chair', 'Couch', 'Table', 'Wardrobe',
              'Bee', 'Beetle', 'Butterfly', 'Caterpillar', 'Cockroach', 'Bear', 'Leopard', 'Lion', 'Tiger', 'Wolf', 'Bridge', 'Castle', 'House',
              'Road', 'Skyscraper', 'Cloud', 'Forest', 'Mountain', 'Plain', 'Sea', 'Camel', 'Cattle', 'Chimpanzee', 'Elephant', 'Kangaroo', 'Fox',
              'Porcupine', 'Possum', 'Raccoon', 'Skunk', 'Crab', 'Lobster', 'Snail', 'Spider', 'Worm', 'Baby', 'Boy', 'Girl', 'Man', 'Woman',
              'Crocodile',  'Dinosaur', 'Lizard', 'Snake', 'Turtle', 'Hamster', 'Mouse', 'Rabbit', 'Shrew', 'Squirrel', 'Maple', 'Oak', 'Palm', 'Pine',
              'Willow', 'Bicycle', 'Bus', 'Motorcycle', 'Pickup truck', 'Train', 'Lawn_mower', 'Rocket', 'Streetcar', 'Tank', 'Tractor']
