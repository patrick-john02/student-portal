<script lang="ts">
export const description = "Sections management page"
export const iframeHeight = "800px"
export const containerClass = "w-full h-full"
</script>

<script setup lang="ts">
import { ref } from "vue"

import AppSidebar from "@/components/sidebars/AppSidebar.vue"
import {
  SidebarProvider,
  SidebarInset,
  SidebarTrigger,
} from "@/components/ui/sidebar"

import {
  Breadcrumb,
  BreadcrumbItem,
  BreadcrumbList,
  BreadcrumbLink,
  BreadcrumbPage,
  BreadcrumbSeparator,
} from "@/components/ui/breadcrumb"

import { Separator } from "@/components/ui/separator"
import {
  Card,
  CardHeader,
  CardTitle,
  CardDescription,
  CardContent,
} from "@/components/ui/card"

import { Button } from "@/components/ui/button"
import { Badge } from "@/components/ui/badge"
import { Input } from "@/components/ui/input"

import {
  Table,
  TableHeader,
  TableRow,
  TableHead,
  TableBody,
  TableCell,
} from "@/components/ui/table"

import {
  DropdownMenu,
  DropdownMenuTrigger,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuLabel,
  DropdownMenuSeparator,
} from "@/components/ui/dropdown-menu"

import { Plus, Users, MoreHorizontal } from "lucide-vue-next"

const userRole = "Admin"

// Dummy data
const sections = ref([
  {
    id: 1,
    name: "Grade 11 – STEM A",
    level: "Grade 11",
    adviser: "Maria Santos",
    students: 45,
    color: "bg-blue-500",
  },
  {
    id: 2,
    name: "Grade 11 – HUMSS B",
    level: "Grade 11",
    adviser: "Juan Dela Cruz",
    students: 38,
    color: "bg-green-500",
  },
  {
    id: 3,
    name: "Grade 12 – ABM A",
    level: "Grade 12",
    adviser: "Ana Reyes",
    students: 42,
    color: "bg-yellow-500",
  },
  {
    id: 4,
    name: "Grade 12 – GAS C",
    level: "Grade 12",
    adviser: "Robert Garcia",
    students: 40,
    color: "bg-red-500",
  },
])

const search = ref("")
</script>

<template>
  <SidebarProvider>
    <AppSidebar :userRole="userRole" />

    <SidebarInset>
      <!-- Header -->
      <header
        class="flex h-16 shrink-0 items-center gap-2 px-4 transition-all"
      >
        <SidebarTrigger class="-ml-2" />
        <Separator orientation="vertical" class="mx-2 h-4" />

        <Breadcrumb>
          <BreadcrumbList>
            <BreadcrumbItem>
              <BreadcrumbLink href="/admin/dashboard">Admin</BreadcrumbLink>
            </BreadcrumbItem>
            <BreadcrumbSeparator />
            <BreadcrumbItem>
              <BreadcrumbPage>Sections</BreadcrumbPage>
            </BreadcrumbItem>
          </BreadcrumbList>
        </Breadcrumb>
      </header>

      <!-- Content -->
      <div class="flex flex-1 flex-col gap-4 p-4 pt-0">
        <!-- Top Bar -->
        <div class="flex items-center justify-between">
          <div>
            <h2 class="text-2xl font-bold tracking-tight">Sections</h2>
            <p class="text-sm text-muted-foreground">
              Manage grade levels, sections, and class advisers.
            </p>
          </div>

          <Button class="flex items-center gap-2">
            <Plus class="h-4 w-4" />
            Add Section
          </Button>
        </div>

        <Card>
          <CardHeader>
            <CardTitle>Sections Overview</CardTitle>
            <CardDescription>
              View, edit, or remove class sections.
            </CardDescription>
          </CardHeader>

          <CardContent>
            <!-- Search -->
            <div class="flex items-center justify-between mb-4">
              <Input
                v-model="search"
                placeholder="Search sections..."
                class="max-w-xs"
              />
            </div>

            <!-- Table -->
            <Table>
              <TableHeader>
                <TableRow>
                  <TableHead class="w-56">Section</TableHead>
                  <TableHead>Adviser</TableHead>
                  <TableHead class="text-center w-28">Students</TableHead>
                  <TableHead class="text-right w-20">Actions</TableHead>
                </TableRow>
              </TableHeader>

              <TableBody>
                <TableRow
                  v-for="section in sections"
                  :key="section.id"
                  class="hover:bg-muted/50"
                >
                  <TableCell>
                    <div class="flex items-center gap-2">
                      <div
                        class="h-3 w-3 rounded-full"
                        :class="section.color"
                      ></div>
                      <div>
                        <p class="font-medium">{{ section.name }}</p>
                        <p class="text-xs text-muted-foreground">
                          {{ section.level }}
                        </p>
                      </div>
                    </div>
                  </TableCell>

                  <TableCell class="text-muted-foreground">
                    {{ section.adviser }}
                  </TableCell>

                  <TableCell class="text-center">
                    <Badge variant="secondary">
                      <Users class="h-3 w-3 mr-1" />
                      {{ section.students }}
                    </Badge>
                  </TableCell>

                  <TableCell class="text-right">
                    <DropdownMenu>
                      <DropdownMenuTrigger as-child>
                        <Button variant="ghost" size="icon">
                          <MoreHorizontal class="h-4 w-4" />
                        </Button>
                      </DropdownMenuTrigger>

                      <DropdownMenuContent align="end">
                        <DropdownMenuLabel>Actions</DropdownMenuLabel>
                        <DropdownMenuSeparator />

                        <DropdownMenuItem>Edit Section</DropdownMenuItem>
                        <DropdownMenuItem>Assign Students</DropdownMenuItem>
                        <DropdownMenuSeparator />
                        <DropdownMenuItem class="text-red-600"
                          >Delete Section</DropdownMenuItem
                        >
                      </DropdownMenuContent>
                    </DropdownMenu>
                  </TableCell>
                </TableRow>
              </TableBody>
            </Table>
          </CardContent>
        </Card>
      </div>
    </SidebarInset>
  </SidebarProvider>
</template>
