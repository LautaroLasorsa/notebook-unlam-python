cp $1.py $1.print; for x in $1*.in; do echo ARCHIVO: $x; cat $x; echo ===; python3 $1.py<$x; echo ===; done | tee -a $1.print

# Uso: ./run.sh nombre_programa
# Notar que no ponemos nombre_programa.py, sino solo nombre programa
# Importante: Los casos de prueba deben estar en el mismo directorio que el programa
# Los archivos de entrada deben tener la extensión .in
# Ej: ./run.sh A para ejecutar el programa A.py con los casos de prueba A1.in, A2.in, etc.