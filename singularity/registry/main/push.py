'''

Copyright (C) 2017 The Board of Trustees of the Leland Stanford Junior
University.
Copyright (C) 2016-2017 Vanessa Sochat.

This program is free software: you can redistribute it and/or modify it
under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or (at your
option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Affero General Public
License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.

'''

from singularity.logger import bot
from singularity.registry.client import Client
import sys
import pwd
import os


def main(args,parser,subparser):

    # Does the user have a valid image?
    image = args.image[0]
    if not os.path.exists(image):  
        subparser.print_help()
        bot.error("Please supply one or more paths to existing images.")
        sys.exit(1)

    
    # Authenticate
    sreg = Client(secrets=args.secrets)
    response = sreg.push(path=image,
                         name=args.name,
                         tag=args.tag,
                         compress=args.compress)
