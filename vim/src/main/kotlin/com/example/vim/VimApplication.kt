package com.example.vim

import com.example.vim.dao.ProviderRepository
import org.springframework.boot.CommandLineRunner
import org.springframework.boot.autoconfigure.SpringBootApplication
import org.springframework.boot.runApplication
import org.springframework.beans.factory.annotation.Autowired


@SpringBootApplication
class VimApplication : CommandLineRunner {
    @Autowired
    lateinit var providerRepo: ProviderRepository

    override fun run(vararg args: String?) {
        providerRepo.initProviders()
    }
}

fun main(args: Array<String>) {
    runApplication<VimApplication>(*args)
}
