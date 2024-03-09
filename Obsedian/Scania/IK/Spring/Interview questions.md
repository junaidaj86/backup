
1. Why will you choose spring boot over spring mvc?
		1. Dependency resolution / version conflict : If we are using spring mvc, then we have to remember all the internal decency and add them. Along with that we have to add the version of each dependency. WIth SPring boot we have starter package which will inturn add all dependency. also we dont mention the version, we select the parent version and it will take care of dependency and version.
		2. Avoid additional configurations: if we want database functionality we have to create data source, session factory adn transactional manager. in Spring boot we just give the property name and spring will inturn create all the above beans
		3. Embedded tomcat / jettyserver in spring boot, but in spring mvc we have to deploy the war file
		4. Spring boot provide productin ready features like health and metrics out of box.

2.  Which spring boot modules have you used?
		1. Spring boot starter  web
		2. Spring boot starter data JPA
		3. Spring boot starter AOP
		4. Spring boot starter security
		5. Spring boot starter for Apache kafka
3. How do you run spring boot application?
		we run from IDE or using maven plugin mvn spring-boot:run
		this will pick the file form target folder which is created when we run mvn run build
4. Why do we use @Springbootapplication: This is combiniation of 3 annotation
		1. @ComponentScan : tell spring where to look for all beans
		2. @EnableAUtoConfiguration
		3. @SprinbootConfiguration: tell spring if we have added 3rd party bean classes
5.  WHat is auto configurations in spring boot: When we add dependency in spring boot we get out of box beans, these beans are created by @EnableAUtoConfiguration. we can see it has some positive match and negative match.  all beans will be created based on some conditions. for example, if we want o auto congifure jaxson object parser, condition is the calss should have ObjectMapper.class in it.
6. How to disable some beans from being auto configured? we can in main class in annotation @SPringbootApplication(exclude {DataSourceAutoConfiguration.class}) and this bean will not be auto loaded. or in app.properties file spring.autoconfigure.exclude= DataSourceAutoConfiguration.class
7. what does spring boot main class do? first it loads all props in .prop or yaml file, then create applicationContext, then creats all auto config beans then refresh all context adn app is ready to use.then deploy in tomcat8. 
8. what is commadnlinerunner? in springboot main class we use this. its an finctional inetyrface with single method run
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class MySpringBootApplication {

    public static void main(String[] args) {
        SpringApplication.run(MySpringBootApplication.class, args);
    }

    // Anonymous inner class implementation of CommandLineRunner
    CommandLineRunner myCommandLineRunner() {
        return args -> {
            // Code to be executed after the application context is initialized
            System.out.println("Executing MyCommandLineRunner. Application started!");

            // You can add your logic here, for example, loading initial data, setting up configurations, etc.
        };
    }
}


