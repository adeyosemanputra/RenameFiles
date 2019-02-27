import os, sys;

arguments = len(sys.argv);
if arguments < 2:
     depth = 0;
else:
     depth = int(sys.argv[1]);
if arguments < 3:
     current_directories = ['.'];
else:
     current_directories = sys.argv[2:];

def loop_dir(directory, depth):
     if directory == '.':
	      directory = os.getcwd();

     print(directory);
     for file_name in os.listdir(directory):
          file_path = directory + '\\' + file_name;
          if os.path.isdir(file_path):
               if depth == -1:
                    loop_dir(file_path, depth);
               elif depth > 0:
                    loop_dir(file_path, depth - 1);
               else:
                    print('Depth limit reached');
          elif os.path.isfile(file_path):
               counter = 1;
               file_extension = os.path.splitext(file_name)[1];
               new_filename = directory + '\\' + directory + file_extension;
               while (os.path.isfile(new_filename)):
                    new_filename = directory + '\\' + directory + '-' + str(counter) + file_extension;
                    counter = counter + 1;
               os.rename(file_path, new_filename);
               print(file_path + " renamed to " + new_filename);


for current_directory in current_directories:
     loop_dir(current_directory, depth);
