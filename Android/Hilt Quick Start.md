1. dependency
```
implementation "com.google.dagger:hilt-android:$hilt_version"
kapt "com.google.dagger:hilt-compiler:$hilt_version"
```

2. Attach `@HiltAndroidApp` at your Application class

```kotlin
import android.app.Application
import dagger.hilt.android.HiltAndroidApp

// don't forget to write to Manifest.xml also
@HiltAndroidApp
class TodoApplication :Application() {

}
```

3. Module Class
```kotlin
@dagger.Module
@InstallIn(SingletonComponent::class)
object Module {
    // define 'How to create Instance'
    @Provides
    fun provideDatabase(@ApplicationContext context: Context) = Room.databaseBuilder(context, AppDatabase::class.java, "task_database").build()
}
```

4. EntryPoint attaches to MainActivity
```kotlin
@AndroidEntryPoint
class MainActivity : ComponentActivity() {
    //...
}
```

5. Constructor Injection Example
```kotlin
@HiltViewModel
class MainViewModel @Inject constructor(private val taskDao: TaskDao) : ViewModel() {
  //... you can use 'taskDao' in class without creating instance
}
```
