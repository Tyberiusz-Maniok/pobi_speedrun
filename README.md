##execution

pyhon3 pobi_speedrun.py path/to/your/project class_name first_param:type second_param:type ...

*project directory must contain include and src directories*

##example

python3 pobi_speedrun.py ./my_project my_class my_param1:int my_param2:string

will generate ./my_project/include/my_class.h and ./my_project/src/my_class.cpp files
containing class declaration and implementation respectively: includes constructor, destructor and getters
