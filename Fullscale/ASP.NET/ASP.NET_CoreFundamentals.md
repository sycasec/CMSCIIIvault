[[ASP.NET]]
```toc
```


- pages by default use the `_layouts.cshtml` to render index
- `asp-page` keyword injects a razor page with the same name into the page

## Entity Framework
- add `EntityFramework.Core` as dependency into specific project


## Dependency Injection
```C#
public void ConfigureServices(IServiceCollection services){
	//register framework services
	services.AddMvc();

	//register our own services
	services.AddScoped<InterfaceServiceClass, ActualServiceClass>();
} 
```
- creates loose coupling of classes
- allows our service to be accessible throughout all the projects without being manually instantiated
- our service provider returns an instance usable through dependency injection
### `AddTransient<>()`
- returns a new clean instance of the service every time we inject it ( or each time it is requested )
- most useful when service contains mutable state and is not thread safe
- potentially less efficient
### `AddSingleton<>()`
- returns a singleton instance, the same instance we use everywhere it is asked.
- allocates less objects and reduces load on Garbage Collector
- Must be thread-safe
- suited to functional stateless services
### `AddScoped<>()`
- services created once per request
- lives in scope
- MVC creates one instance per HTTP request
	- uses same instance in other calls within the same web request
### Injection
- Dependency can now be injected in specific classes

### Service Descriptors
- holds details about registered services
	- `Type ImplementationType`
	- `Type ServiceType`
	- `ServiceLifetime Lifetime`
- auto created by `IService`
- 
## MVC
### Models
- contains domain data and logic that manages the data
- hides details of how data operations from customer

### Controller
- uses model and view to respond to user action
- directly interacts with model
- does not need to know about the data

- worked on ASP.NET Core 3 Intermediate Path