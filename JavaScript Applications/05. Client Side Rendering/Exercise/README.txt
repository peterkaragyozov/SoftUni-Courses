Hello,

If you're using VSC, I suggest opening the whole folder in VSC instead of opening each solution as a separate project.

The node_modules folder serves as a common one for all the projects, so it is not necessary to install a separate one for each project.

When starting lite-server for the whole folder, access to each solution occurs through the following URLs:

http://localhost:3000/01.List-Towns/index.html
http://localhost:3000/02.HTTP-Status-Cats/index.html
http://localhost:3000/03.Search-in-List/index.html
http://localhost:3000/04.Fill-Dropdown/index.html
http://localhost:3000/05.Table-Search/index.html
http://localhost:3000/06.Book-Library/index.html