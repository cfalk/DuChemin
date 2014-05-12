from django.core.management.base import BaseCommand, CommandError
from duchemin.models.piece import DCPiece
from shutil import copyfile
import os

class Command(BaseCommand):
  help = "Imports/Replaces an MEI/PDF/MP3 file related to a specific piece."
  
  def handle(self, *args, **kwargs):
    arg_guide = "<piece id> <new_file> <file_type>"

    #Validate that there are three args.
    if len(args)!=3:
      self.stdout.write("Requires 3 parameters: {}".format(arg_guide))
      return 

    #Collect the piece.
    try:
      piece = DCPiece.objects.filter(piece_id=args[0])[0]
    except:
      raise CommandError("Piece not found with that piece_id.")

    #Verify that the specified type is added.
    if arg[2].lower() in {"mp3", "mei", "pdf"}:
      ext = arg[2].lower()
    else:
      raise CommandError("Illegal file type! Choices are: MP3, MEI, PDF.")
      
    try:
      file_name = "{}{}E.{}".format(MEDIA_ROOT, piece.piece_id, ext)
      #Request over-write confirmation if the file already exists.
      if os.path.isfile(file_name):
       if input("File exists! Okay to over-write? [y/n]").lower()[0] != "y":
        self.stdout.write("Operation aborted!")
        return  

      #Actually write the file.
      copyfile(args[1], file_name)

      #Get the old_file if applicable.
      old_file = getattr(piece, ext+"_file")

      #Store the URLField for the modified piece.
      #  NOTE: This implementation retains "replaced" files in the system.
      setattr(piece, ext+"_file", file_name)
      piece.save()
      
      #Uncomment the following 2 lines to enable deletion of "replaced" files.
      #if old_file:
      #  os.remove(old_file)

      self.stdout.write("File imported successfully!")
    except:
      raise CommandError("File could not be written.")
