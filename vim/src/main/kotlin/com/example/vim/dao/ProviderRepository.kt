package com.example.vim.dao

import com.example.vim.model.Provider
import com.fasterxml.jackson.module.kotlin.jacksonObjectMapper
import com.fasterxml.jackson.module.kotlin.readValue
import com.fasterxml.jackson.module.kotlin.registerKotlinModule
import org.springframework.stereotype.Repository
import java.io.File

@Repository
class ProviderRepository {
    var providers: List<Provider>? = null

    fun initProviders() {
        val mapper = jacksonObjectMapper()
        mapper.registerKotlinModule()

        //parse providers
        val jsonString: String = File("./src/main/resources/providers.json").readText(Charsets.UTF_8)
        providers = mapper.readValue(jsonString)

        // lower case specialties
        for (provider in providers!!) {
            val lowerCaseSpecialities = provider.specialties.map { specialty -> specialty.toLowerCase() }
            provider.specialties = lowerCaseSpecialities
        }

        // sort by score
        providers = providers!!.sortedByDescending { it.score }

        for (provider in providers!!) {
            println(provider)
        }
    }
}