

# **Análisis Sintáctico Exhaustivo del Context Mapper DSL (CML) para el Desarrollo de un Parser en Python**

El Context Mapper DSL (CML) es un lenguaje de dominio específico (DSL) fundamental para el modelado de arquitecturas basadas en Domain-Driven Design (DDD). Este informe proporciona una descripción exhaustiva de su sintaxis y estructura gramatical, con el fin de servir como referencia técnica para el desarrollo de un *parser* eficiente en el entorno Python.

## **I. Fundamentos Lingüísticos del CML y su Contexto Tecnológico**

El Context Mapper DSL no es un lenguaje diseñado desde cero, sino una composición de múltiples gramáticas y tecnologías preexistentes. Comprender su base tecnológica es esencial para replicar su funcionalidad de *parsing* y generación de modelos semánticos.

### **A. La Arquitectura de CML y su Origen Xtext**

El CML fue desarrollado utilizando Xtext, un *framework* para la creación de DSLs textuales que se integra profundamente con el ecosistema Eclipse Modeling Framework (EMF).1 Xtext utiliza un enfoque dual: describe tanto la sintaxis concreta del lenguaje como la manera en que esta sintaxis se mapea a una representación interna en memoria, conocida como el modelo semántico o *Abstract Syntax Tree* (AST).2

La relevancia de esta arquitectura para un *parser* en Python reside en que la meta de *parsing* va más allá de la mera validación sintáctica. El proceso debe generar un gráfico de objetos que represente el modelo de dominio (el *Abstract Semantic Graph* o ASG) con sus referencias resueltas, similar a cómo Xtext infiere el modelo Ecore de EMF.2 Cuando se utilizan herramientas como textX en Python, que están inspiradas en Xtext 4, se busca configurar el *parser* para construir directamente esta estructura de objetos semánticos, omitiendo la necesidad de procesar un *Parse Tree* genérico intermedio. Este enfoque, que prioriza la construcción inmediata del meta-modelo, es crucial para la eficiencia y la utilidad posterior del *parser* en la validación y transformación del modelo DDD.

La gramática de Xtext se especifica utilizando una notación similar a la *Extended Backus-Naur Form* (EBNF).2 Esta notación es fundamental para definir la cardinalidad de los elementos sintácticos, utilizando operadores estándar como ? (cero o uno), \* (cero o más), y \+ (uno o más).2

### **B. Componentes Fundamentales de la Gramática**

El CML se estructura mediante reglas de alto nivel (no terminales) que corresponden directamente a los patrones de DDD, y reglas de bajo nivel (terminales) que definen los *tokens* atómicos.

Las reglas no terminales incluyen elementos esenciales de la arquitectura, como ContextMap, BoundedContext, Relationship, y Aggregate. Estas reglas definen la estructura jerárquica del modelo.

Las reglas terminales abarcan:

1. **Palabras Clave Reservadas:** Términos de DDD o CML (ej., ContextMap, type, implements, Entity, Service).1  
2. **Operadores Delimitadores:** Caracteres que estructuran el código, como llaves ({}), corchetes (\`\`), comas (,), y puntos y comas (;).6  
3. **Operadores de Relación:** Símbolos direccionales (-\>, \<-, \<-\>).8  
4. **Literales:** Tipos básicos como identificadores (IDs), *strings* (delimitados por comillas "), y números.

## **II. La Capa Léxica y Estructura Global del Archivo.cml**

La capa léxica define los elementos básicos que el *parser* debe reconocer. Las decisiones de diseño en CML, particularmente la opcionalidad de ciertos delimitadores, imponen requisitos estrictos al *lookahead* del *parser*.

### **A. Delimitadores, Operadores y Palabras Clave Reservadas**

La tabla a continuación resume los principales delimitadores utilizados en la sintaxis CML. Es notable que ciertos elementos, como el signo de asignación, no son obligatorios, lo que afecta la robustez requerida del *parser*.

Tabla II.1: Delimitadores y Operadores Clave en CML

| Elemento Sintáctico | Función Principal | Opcionalidad | Contexto de Uso |
| :---- | :---- | :---- | :---- |
| {} (Llaves) | Delimitador de bloques (BC, CM, Aggregate) | Obligatorio | Declaración de cuerpos de entidades |
| \= (Igual) | Asignación de valores de atributos | Opcional | Asignación de metadatos (ej., type \= SYSTEM\_LANDSCAPE o type SYSTEM\_LANDSCAPE) 8 |
| , (Coma) | Separador de listas | Obligatorio en listas | Listas de subdominios, agregados, roles de relación 8 |
| : (Dos Puntos) | Nombramiento de relaciones | Opcional | BC1\<-\> BC2 : ModelName 8 |
| " (Comillas) | Delimitador de *strings* | Obligatorio | domainVisionStatement "text..." 9 |
| \[ \] (Corchetes) | Encapsulan roles y patrones de relación | Obligatorio en sintaxis de flechas | Especificación de roles de Context Map 8 |
| \- (Guion/Menos) | Indicador de referencia de tipo de dominio (Sculptor DSL) | Obligatorio para referencias | Usado dentro de Aggregates para atributos que referencian entidades o VOs 10 |

### **B. Reglas de Opcionalidad y Ambientes Lexicales**

Una característica distintiva del CML, heredada de Xtext, es la flexibilidad en la asignación de atributos. El signo igual (=) para asignar valores a los atributos puede ser omitido.8 Por ejemplo, ambas sintaxis son válidas:

Fragmento de código

type \= SYSTEM\_LANDSCAPE  
type SYSTEM\_LANDSCAPE

Para implementar un *parser* confiable, especialmente con herramientas basadas en PEG (Parsing Expression Grammars) como textX, esta opcionalidad requiere una definición gramatical precisa. El *parser* debe tener suficiente *lookahead* para distinguir si la cadena de texto que sigue a un atributo (como type o state) es el valor esperado (un ID, un *String*, o un Enum) o el inicio de una nueva declaración de alto nivel (por ejemplo, el *keyword* BoundedContext o la llave { que comienza un bloque). La robustez del *parser* depende de gestionar correctamente el límite entre un valor de atributo omitido y el siguiente token léxico significativo.

Además, los elementos principales como ContextMap y BoundedContext pueden ser declarados con un nombre opcional inmediatamente después de su palabra clave.8

### **C. Estructura de Módulos y la Directiva import**

CML soporta la modularización del modelo a través de la directiva import.1 Esto permite que los BoundedContexts sean definidos en archivos separados (.cml) y reutilizados en múltiples ContextMaps.11

La sintaxis de importación es simple, típicamente utilizando rutas relativas:

Fragmento de código

import "./BoundedContexts/CustomerManagement.cml"

Aunque es posible importar archivos de diferentes directorios, se impone una restricción estructural: un único archivo .cml solo puede contener una única declaración de ContextMap.11

El desarrollo de un *parser* en Python que maneje esta modularidad debe incorporar una fase de pre-procesamiento o carga recursiva. El sistema debe identificar todas las sentencias import, cargar los archivos referenciados, y consolidar un modelo unificado de todos los BoundedContexts definidos. Este modelo consolidado es fundamental, ya que las referencias cruzadas y las relaciones en el ContextMap principal (fase de *linking*) solo pueden resolverse con éxito si todos los elementos constituyentes están disponibles en la memoria.

## **III. Gramática del DDD Estratégico (Reglas de Nivel Superior)**

Los elementos estratégicos son la columna vertebral del CML y se definen en el nivel superior del archivo.

### **A. Bounded Context (BC)**

El BoundedContext es la unidad fundamental de encapsulación en DDD. Su declaración en CML es rica en metadatos y actúa como el punto de transición hacia el modelado táctico.9

**Sintaxis de Declaración:** Un BC se declara utilizando el *keyword* BoundedContext, seguido de su nombre (opcionalmente) y su cuerpo delimitado por llaves {}.

Fragmento de código

BoundedContext ContextMapperTool refines StrategicDomainDrivenDesignContext {... }

El nombre de un BoundedContext debe ser único dentro de todo el modelo CML.9

**Metadatos Estructurales:**

* **implements**: Especifica los Domain o Subdomain (separados por comas) que el BC implementa.9  
* **refines**: Permite que un BC herede o mejore otro BC, aunque las reglas tácticas internas (Aggregates) no se resuelven recursivamente por los generadores.9

Atributos Opcionales (Metadatos):  
El CML soporta numerosos atributos para la documentación y la validación, incluyendo:

* type: Define la función del BC (ej., FEATURE, SYSTEM).9  
* domainVisionStatement: Documenta el propósito del BC.9  
* implementationTechnology: Describe la tecnología utilizada (ej., "Java, Eclipse").9  
* responsibilities: Una lista de responsabilidades asociadas al contexto.12  
* knowledgeLevel: Define el nivel de conocimiento (CONCRETE o ABSTRACT).1  
* realizes: Este *keyword* se utiliza para indicar qué BoundedContexts son implementados por un BC de tipo TEAM. Una restricción semántica impone que realizes solo puede ser utilizado si el type del BC es TEAM.9

El cuerpo del BoundedContext es la puerta de entrada a la gramática de segundo nivel, el Sculptor DSL. Dentro de este bloque, se pueden anidar los patrones tácticos como Module y Aggregate.9 Esto requiere que el *parser* gestione el cambio de contexto sintáctico y de reglas de alcance.

### **B. Context Map (CM)**

El ContextMap es el elemento organizativo más importante, ya que define las relaciones entre los BoundedContexts.8

**Sintaxis de Declaración:** ContextMap \[Name\]? { \[Attributes\]\[Contains\] }.8 El nombre es opcional.8

**Atributos de CM:**

* type: Define si el mapa modela sistemas (SYSTEM\_LANDSCAPE) o equipos (ORGANIZATIONAL/Team Map).8  
* state: Indica si el mapa es el estado actual (AS\_IS) o deseado (TO\_BE).8

**Inclusión de Contextos:** Los BoundedContexts se añaden al mapa usando el *keyword* contains. Se puede usar múltiples instancias de contains o listar los BCs separados por comas 8:

Fragmento de código

ContextMap {  
  contains CargoBookingContext, VoyagePlanningContext  
}

Es importante señalar que existe una restricción semántica estricta en la interacción entre tipos: un BoundedContext de tipo TEAM no puede ser contenido dentro de un ContextMap de tipo SYSTEM\_LANDSCAPE.13 Esta validación se ejecuta típicamente después de que el *parser* haya construido el AST, asegurando la coherencia en el modelado arquitectónico.

## **IV. Gramática de las Relaciones de Context Map (Operadores y Patrones)**

La definición de relaciones es la parte más compleja del CML, ya que codifica patrones de interacción estratégicos (Shared Kernel, Partnership, Customer/Supplier) y roles de implementación (ACL, OHS, PL, CF) en una sintaxis compacta que combina operadores direccionales y *tokens* posicionales dentro de corchetes.

### **A. Estructura General de la Relación**

Todas las relaciones, salvo la sintaxis de palabras clave, siguen una estructura fija:

$$\\text{BC\\\_A } \\text{ Operador } \\text{ BC\\\_B }? \\{ \\text{ Attributes } \\}$$  
.8

### **B. Relaciones Simétricas (Partnership y Shared Kernel)**

Las relaciones simétricas utilizan el operador bidireccional \<-\>.8 Los roles dentro de los corchetes deben ser idénticos en ambos lados:

* **Shared Kernel (SK):** BC\_A\<-\> BC\_B.8  
* **Partnership (P):** BC\_A \[P\]\<-\>\[P\] BC\_B.

### **C. Relaciones Asimétricas (Upstream-Downstream Genéricas)**

Las relaciones asimétricas (U/D) definen un flujo de influencia. La flecha (-\>) siempre apunta del contexto *Upstream* (el proveedor) al *Downstream* (el consumidor).8

**Notación de Flechas (con roles U/D):**

1. Upstream a Downstream: BC\_Upstream \[U\]-\> BC\_Downstream  
2. Downstream a Upstream: BC\_Downstream\<-\[U\] BC\_Upstream.8

Notación de Palabras Clave (Keywords):  
El CML también permite el uso de palabras clave equivalentes a los operadores de flecha, lo cual puede mejorar la legibilidad del modelo:

3. BC\_Upstream Upstream-Downstream BC\_Downstream  
4. BC\_Downstream Downstream-Upstream BC\_Upstream.8

### **D. La Relación Customer/Supplier (C/S)**

La relación *Customer/Supplier* es una forma especializada de U/D, donde las prioridades del *Customer* (Downstream) influyen en la planificación del *Supplier* (Upstream). Sintácticamente, se distingue por la inclusión de los roles S (Supplier) y C (Customer).8

**Sintaxis Completa (con U/D y S/C):**

* CustomerSelfServiceContext\<- CustomerManagementContext.8

Los roles U y D son opcionales si se utilizan S y C, pero su inclusión es una práctica común para la claridad del modelo.8 También existe la sintaxis alternativa con palabras clave:

* CustomerSelfServiceContext Customer-Supplier CustomerManagementContext.8

### **E. Integración de Patrones de Intercambio (OHS, PL, ACL, CF)**

Los patrones de integración (OHS, PL, ACL, CF) se especifican dentro de los corchetes de rol, junto con los identificadores de direccionalidad (U, D, S, C). Para un *parser* robusto, es crucial que se reconozca que existe una jerarquía implícita de tokens dentro del corchete (separados por comas).8

**Roles por Contexto:**

* **Upstream/Supplier:** OHS (Open Host Service) y PL (Published Language).  
* **Downstream/Customer:** CF (Conformist) y ACL (Anti-Corruption Layer).

**Ejemplo de roles combinados:** VoyagePlanningContext\<- LocationContext.8

El parser debe estar diseñado para manejar la lista de tokens separados por comas. El sistema debe distinguir primero los tokens estructurales (U, D, S, C) y luego los patrones de interacción (OHS, PL, ACL, CF).

#### **Atributos de Relación y Referencias Cruzadas**

Las relaciones pueden tener un bloque de cuerpo {} opcional para definir atributos adicionales 8:

1. implementationTechnology (String).  
2. downstreamRights (Enum, ej., VETO\_RIGHT, INFLUENCER).  
3. exposedAggregates: Una lista de referencias a Aggregates que el contexto *Upstream* expone al *Downstream*.8

El atributo exposedAggregates representa un desafío significativo en la fase de construcción del modelo semántico. La referencia al Aggregate no es local, sino que debe vincularse a la definición real del objeto Aggregate que reside *dentro* del BoundedContext identificado como Upstream. Esto impone la necesidad de una fase de resolución de referencias cruzadas (o *linking*) después del *parsing* inicial, una tarea central que el *parser* en Python debe replicar del comportamiento Xtext/EMF.8

Aunque la sintaxis de CML es permisiva, la documentación de Context Mapper establece reglas semánticas estrictas (ej., el patrón *Conformist* no es aplicable en una relación *Customer/Supplier*). El *parser* debe enfocarse en la validez sintáctica y la correcta construcción del ASG, delegando la detección de estas contradicciones de DDD (que a menudo resultan en advertencias, no errores de compilación) a una capa de validación de modelo posterior.

La siguiente tabla resume la matriz de operadores y roles, crucial para la lógica de *parsing*:

Tabla IV.1: Matriz de Operadores de Relación y Roles de Context Map (DDD Estratégico)

| Tipo | Operador Central | Rol Upstream/Supplier (Posición 1\) | Rol Downstream/Customer (Posición 1\) | Roles de Intercambio (Posición 2+) |
| :---- | :---- | :---- | :---- | :---- |
| Shared Kernel (SK) | \<-\> | \`\` | \`\` | Ninguno |
| Partnership (P) | \<-\> | \[P\] | \[P\] | Ninguno |
| U/D Genérica | \-\> o \<- | \[U\], opc. \`\` | , opc. | OHS, PL (Upstream); ACL, CF (Downstream) |
| Customer/Supplier (C/S) | \-\> o \<- | opc. | opc. | PL (Supplier); ACL (Customer) |

## **V. Gramática del DDD Táctico (La Inclusión del Sculptor DSL)**

El modelado DDD Táctico dentro de un BoundedContext se basa en gran medida en la reutilización de la gramática Sculptor DSL.1 Esto configura el CML como un DSL híbrido, donde el *parser* debe cambiar su contexto de reglas al descender al cuerpo de un BoundedContext.

### **A. La Adaptación del Patrón Aggregate en CML**

Mientras que la mayoría de los patrones tácticos siguen la sintaxis pura de Sculptor, el Aggregate es la única regla adaptada por CML.7 El nombre del Aggregate debe ser único en todo el modelo CML.7

Extensiones CML para Aggregate:  
El CML extiende el Aggregate con capacidad para soportar los patrones Responsibility Layers y Knowledge Level 7:

* responsibilities: Define una lista de cadenas de texto.7  
* knowledgeLevel: Asigna un nivel de conocimiento (ej., CONCRETE).7

El Aggregate contiene los bloques tácticos de Sculptor, incluyendo Services, Resources, Consumers y SimpleDomainObjects (Entities, Value Objects, Domain Events).7 También soporta un mecanismo crucial para el modelado de estados: el ciclo de vida del agregado. Esto se define mediante un enum interno marcado con el *keyword* aggregateLifecycle, listando los estados disponibles.7

Fragmento de código

enum States {  
  aggregateLifecycle   
  CREATED, POLICE\_CREATED, RECALLED  
}

### **B. Modelado de Objetos de Dominio Simple (Sculptor DSL)**

La sintaxis para la definición de los objetos tácticos se toma directamente de Sculptor.10

* **Entity:** Declarado con el *keyword* Entity. Puede incluir el *keyword* aggregateRoot para designar la entidad principal del Aggregate.10  
* **Value Object (VO):** Declarado con ValueObject. Los atributos pueden ser marcados como key.7  
* **Atributos:** Los atributos se declaran siguiendo el patrón \[Name\]. Se admiten tipos primitivos (String, int, boolean) y colecciones (List, Set, Bag).10

### **C. Mecanismos de Referencia de Tipos dentro de Sculptor**

Una convención sintáctica crucial que el *parser* debe manejar en la capa táctica es la forma de referenciar otros objetos de dominio (Entities, VOs) versus la declaración de tipos primitivos o locales.

El signo menos (-) actúa como un indicador de referencia. Si un atributo en la capa táctica referencia un tipo de dominio ya definido, debe precederse con \-.10

Tabla V.2: Reglas de Sintaxis Táctica y Referencia de Tipos (Sculptor Adaptation)

| Sintaxis de Atributo | Presencia de \- | Tipo de Dato | Implicación para el Parser | Ejemplo CML |
| :---- | :---- | :---- | :---- | :---- |
| \[Name\] | Ausente | Primitivo o tipo local | No requiere resolución de referencia cruzada interna. | String firstname 10 |
| \-\[Name\] | Presente | Tipo de dominio (Entity, VO, etc.) | Requiere una fase de *linking* para resolver RefType dentro del modelo. | \- SocialInsuranceNumber sin 10 |
| \- List\<\> \[Name\] | Presente | Colección de tipos de dominio | Requiere *linking* para resolver RefType. | \- List\<Address\> addresses 10 |

### **D. Definición de Servicios y Operaciones**

Los servicios de dominio se definen usando el *keyword* Service y pueden contener operaciones (métodos).7

**Sintaxis de Operación General:**

$$\\text{\[OperationName\] (\[ParameterName\],...) \[throws Exception\]? ; }$$  
.10

El tipo de retorno o los parámetros pueden usar el prefijo @ para hacer referencia a tipos de dominio.7

**Micro-DSL de Transiciones de Estado:**

El CML extiende las operaciones de Service con un *micro-DSL* embebido para modelar las transiciones del Aggregate Lifecycle.7 Esto se logra especificando si la operación es de lectura (read-only) o escritura (write), y opcionalmente definiendo la transición de estado usando corchetes \`\`:

$$\\text{\[OpName\] (...) : \[read-only | write\]? \-\>? ; }$$  
Por ejemplo: boolean createPolicy(@ContractId contractId) : write;.7

El *parser* debe estar diseñado para reconocer esta sub-gramática de transición de estados como parte integral de la producción de Service Operation, lo que garantiza que la información del ciclo de vida del agregado se capture en el ASG. La gestión exitosa de la gramática híbrida CML-Sculptor implica la identificación precisa de los puntos de enganche donde la gramática maestra cede el control a las producciones tácticas derivadas de Sculptor.

## **VI. Estrategias de Implementación del Parser en Python**

El desarrollo de un *parser* para CML en Python debe abordar directamente los desafíos impuestos por la arquitectura Xtext: la construcción del modelo semántico y la resolución de referencias cruzadas en un entorno de lenguajes híbridos.

### **A. La Necesidad de un Meta-Modelo (AST) y la Influencia de Xtext**

Dada la génesis del CML en Xtext y EMF, el principal objetivo de la implementación en Python es producir un *Abstract Semantic Graph* (ASG), que es una estructura de objetos que refleja los conceptos de DDD (Bounded Contexts, Relationships, Aggregates) y no un simple *Parse Tree*.2 La estructura de salida debe facilitar el recorrido y la manipulación programática, especialmente para la validación de reglas de dominio o la generación de código.

La gestión de referencias cruzadas es el requisito más técnico. Elementos como exposedAggregates 8 o las referencias internas con guion (-) 10 son simplemente cadenas de texto durante el *parsing* inicial. El *parser* de Python debe implementar una fase de *linking* post-parsing para buscar estos identificadores textuales en el modelo global de BCs y Aggregates y reemplazarlos por punteros a los objetos de destino correspondientes.

### **B. Evaluación de Opciones para Python**

Para replicar la funcionalidad de un *parser* Xtext en Python, se evalúan principalmente dos herramientas:

1. **textX:** textX está conceptualmente alineado con la filosofía Xtext, ya que su objetivo es generar automáticamente un meta-modelo (ASG) a partir de la descripción gramatical.4 Utiliza PEG (Parsing Expression Grammars), lo que elimina ambigüedades comunes en CFG y simplifica el manejo de sintaxis flexibles como la opcionalidad del signo igual (=).4 La rapidez de desarrollo (*grammar interpreter style*) y la construcción automática del modelo de objetos hacen de textX la opción predilecta para replicar la experiencia de un DSL basado en Xtext.  
2. **ANTLR:** ANTLR es un potente generador de *parsers* con soporte maduro para Python.15 Si bien es perfectamente capaz de manejar la complejidad gramatical de CML, genera tradicionalmente un *Parse Tree* genérico. El desarrollador tendría que escribir manualmente una capa completa de *listener* o *visitor* para transformar este árbol en el ASG de objetos DDD requerido, incrementando el esfuerzo de desarrollo y mantenimiento en comparación con textX.4

### **C. Recomendaciones para el Manejo de la Gramática Híbrida**

La estrategia de implementación debe manejar explícitamente la naturaleza híbrida CML-Sculptor:

1. **Integración Gramatical:** La gramática CML maestra debe definir la estructura estratégica (Context Maps, Bounded Contexts). Dentro de las producciones de BoundedContext y Aggregate, el parser debe hacer la transición hacia la gramática táctica derivada de Sculptor para las reglas de Entity, ValueObject, y Service.  
2. **Manejo de *Imports* y Ambientes:** Implementar un mecanismo de carga modular para los archivos importados.11 Este mecanismo debe consolidar todas las definiciones de BoundedContext en un registro global antes de la fase de *parsing* del ContextMap principal y, crucialmente, antes de la fase de *linking*.  
3. **Implementación de Validaciones Semánticas:** Las reglas de diseño de Xtext (que permiten sintaxis pero validan semántica después, como la restricción TEAM/SYSTEM\_LANDSCAPE 13) deben replicarse. El *parser* debe construir el ASG incluso si hay posibles violaciones semánticas, y estas violaciones deben ser marcadas en una fase posterior de validación de modelo, separada del *parsing* sintáctico.

## **VII. Conclusiones y Recomendaciones**

La investigación exhaustiva de la sintaxis del Context Mapper DSL confirma que su gramática es una compleja integración de reglas de alto nivel (Xtext/CML) y reglas de bajo nivel (Sculptor DSL), con requisitos estrictos en la gestión de la opcionalidad léxica y las referencias cruzadas.

1. **Recomendación de Tooling:** Se recomienda enfáticamente el uso de **textX** como *framework* de *parsing* en Python, debido a su alineación conceptual con el modelo Xtext de generación de meta-modelos y su capacidad para manejar gramáticas basadas en PEG sin ambigüedades.  
2. **Arquitectura del Parser:** El parser debe construirse en dos fases primarias:  
   * **Fase 1: Carga y Parsing Sintáctico:** Incluyendo la resolución de la directiva import para consolidar todas las definiciones de BoundedContexts en un pool global.  
   * **Fase 2: Resolución de Referencias (*Linking*):** Implementación de un proceso de vinculación posterior al *parsing* para resolver todas las referencias de tipo (exposedAggregates, referencias con guion en Sculptor) contra el pool global de objetos para construir un ASG completo y conectado.  
3. **Complejidad Gramatical Híbrida:** Es imperativo manejar la transición entre la gramática estratégica y la táctica. El *parser* debe reconocer los elementos CML modificados (especialmente Aggregate con sus atributos responsibilities y knowledgeLevel, y el *micro-DSL* de transición de estados en Services) como reglas específicas, mientras que el resto de los objetos tácticos se rigen por la gramática de Sculptor. La correcta interpretación del token \- en la capa táctica es fundamental para distinguir referencias de tipo de declaraciones de tipos locales.

#### **Obras citadas**

1. CML Reference \- Introduction \- Context Mapper, fecha de acceso: noviembre 21, 2025, [https://contextmapper.org/docs/language-reference/](https://contextmapper.org/docs/language-reference/)  
2. Xtext \- The Grammar Language \- The Eclipse Foundation, fecha de acceso: noviembre 21, 2025, [https://eclipse.dev/Xtext/documentation/301\_grammarlanguage.html](https://eclipse.dev/Xtext/documentation/301_grammarlanguage.html)  
3. The Grammar Language \- Eclipse Help, fecha de acceso: noviembre 21, 2025, [https://help.eclipse.org/latest/topic/org.eclipse.xtext.doc/contents/301\_grammarlanguage.html](https://help.eclipse.org/latest/topic/org.eclipse.xtext.doc/contents/301_grammarlanguage.html)  
4. Comparison \- textX, fecha de acceso: noviembre 21, 2025, [https://textx.github.io/textX/about/comparison.html](https://textx.github.io/textX/about/comparison.html)  
5. textX/textX: Domain-Specific Languages and parsers in Python made easy http://textx.github.io/textX \- GitHub, fecha de acceso: noviembre 21, 2025, [https://github.com/textX/textX](https://github.com/textX/textX)  
6. Delimiters and operators \- IBM, fecha de acceso: noviembre 21, 2025, [https://www.ibm.com/docs/en/epfz/5.3.0?topic=sbcs-delimiters-operators](https://www.ibm.com/docs/en/epfz/5.3.0?topic=sbcs-delimiters-operators)  
7. Aggregate \- Context Mapper, fecha de acceso: noviembre 21, 2025, [https://contextmapper.org/docs/aggregate/](https://contextmapper.org/docs/aggregate/)  
8. Context Mapper, fecha de acceso: noviembre 21, 2025, [https://contextmapper.org/docs/context-map/](https://contextmapper.org/docs/context-map/)  
9. Bounded Context | Context Mapper, fecha de acceso: noviembre 21, 2025, [https://contextmapper.org/docs/bounded-context/](https://contextmapper.org/docs/bounded-context/)  
10. Tactic DDD Syntax \- Context Mapper, fecha de acceso: noviembre 21, 2025, [https://contextmapper.org/docs/tactic-ddd/](https://contextmapper.org/docs/tactic-ddd/)  
11. Imports \- Context Mapper, fecha de acceso: noviembre 21, 2025, [https://contextmapper.org/docs/imports/](https://contextmapper.org/docs/imports/)  
12. Responsibility Layers \- Context Mapper, fecha de acceso: noviembre 21, 2025, [https://contextmapper.org/docs/responsibility-layers/](https://contextmapper.org/docs/responsibility-layers/)  
13. Language Semantics \- Context Mapper, fecha de acceso: noviembre 21, 2025, [https://contextmapper.org/docs/language-model/](https://contextmapper.org/docs/language-model/)  
14. Domain-specific Language and Tools for Strategic Domain-driven Design, Context Mapping and Bounded Context Modeling \- SciTePress, fecha de acceso: noviembre 21, 2025, [https://www.scitepress.org/Papers/2020/89105/89105.pdf](https://www.scitepress.org/Papers/2020/89105/89105.pdf)  
15. ANTLR, fecha de acceso: noviembre 21, 2025, [https://www.antlr.org/](https://www.antlr.org/)